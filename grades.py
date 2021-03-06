from datetime import date

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL

import web_scraper
from collections import namedtuple
from namedlist import namedlist

Subject = namedlist("Subject",
    ["active", "nr", "name", "req", "exam_type", "semester", "grade",
    "status", "credits", "note", "attempt", "date"])

# TODO: translate
Subject.header = ["Count", "Nr", "Name", "Req", "Exam type", "Semester", "Grade",
    "Status", "Credits", "Note", "Attempt", "Date"]

#Subject.visibility = [True, False, True, False, False, False, True,
#    False, True, False, False, False]


class GradesModelProxy(QtGui.QSortFilterProxyModel):
    """This proxy offers column visibility toggling and filtering the data
    from GradesModel.
    """
    def __init__(self, parent=None):
        QtGui.QSortFilterProxyModel.__init__(self, parent)
        self.col_visibility = [True, False, True, False, False, False, True,
            False, True, False, False, False]
        self.setDynamicSortFilter(True)

    def showColumn(self, col_index):
        self.col_visibility[col_index] = True
        self.invalidateFilter()
        self.emit(SIGNAL("columnsVisibilityChanged()"))

    def hideColumn(self, col_index):
        self.col_visibility[col_index] = False
        self.invalidateFilter()
        self.emit(SIGNAL("columnsVisibilityChanged()"))

    def toggleColumn(self, col_index):
        self.col_visibility[col_index] = not self.col_visibility[col_index]
        self.invalidateFilter()
        self.emit(SIGNAL("columnsVisibilityChanged()"))

    def filterAcceptsColumn(self, column, parent):
        return self.col_visibility[column]

    def filterAcceptsRow(self, row, parent):
        # TODO: implement filters
        return True


class GradesModel(QtCore.QAbstractTableModel):
    """A model for grades from the PSSO."""
    def __init__(self, parent=None, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.header_data = Subject.header
        self.subjects = []

    def getFromPSSOIterator(self, username, password):
        """Get grades from PSSO and feed them to the table model.
        This function returns a generator that yields 8 strings describing
        the progress.
        """
        if not username or not password:
            raise ValueError("Please provide valid username and password")
        
        iterator = web_scraper.getHTMLFromPSSOIterator(username, password)
        for i in range(6): # see docs of getHTMLFromPSSOIterator() why 6
            yield iterator.next()
        html = iterator.next() # should be the html doc
        yield "Parsing grades"
        subjects = web_scraper.getSubjectsFromHTML(html)
        self.beginResetModel()
        self.subjects = subjects
        self.endResetModel()
        yield "Done"

    def getFromPSSO(self, username, password):
        """Get grades from PSSO and feed them to the table model."""
        [x for x in self.getFromPSSOIterator(username, password)]

    def getFromHTML(self, html):
        subjects = web_scraper.getSubjectsFromHTML(html)
        self.beginResetModel()
        self.subjects = subjects
        self.endResetModel()

    def rowCount(self, parent):
    	return len(self.subjects)

    def columnCount(self, parent):
    	return len(self.header_data)

    def data(self, index, role):
        row, col = index.row(), index.column()
        if index.isValid() and role == QtCore.Qt.DisplayRole:
            v = QtCore.QVariant(self.subjects[row][col])
            if isinstance(self.subjects[row][col], date):
                v = QtCore.QVariant(QtCore.QDate(self.subjects[row][col]))
            return v
        return QtCore.QVariant()

    def headerData(self, index, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header_data[index]

    def flags(self, index):
        if index.column() == 0:
            return (QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsEditable)
        else:
            return QtCore.Qt.ItemIsEnabled

    def setData(self, index, value, role):
        if role == QtCore.Qt.EditRole:
            row, col = index.row(), index.column()
            if col == 0:
                old = self.subjects[row].active
                new = value.toBool()
                if old != new:
                    self.subjects[row].active = new
                    self.emit(SIGNAL("dataChanged()"))
                    return True
        return False

    def getNumOfGrades(self):
        """Return the number of grades that are marked as active/real."""
        return sum(i.active for i in self.subjects if i.grade and i.credits)

    def getNumOfCredits(self):
        """Return the number of credits earned so far. Only active subjects are
        counted.
        """
        return sum(float(i.credits) for i in self.subjects if i.active)

    def getAverageGrade(self):
        """Return the average grade. Only active subjects are counted.
        The result is rounded by two digits after comma.
        """
        grades_x_credits = 0
        num_credits = 0
        for subj in self.subjects:
            if subj.active and subj.grade and subj.credits:
                grades_x_credits += (subj.grade * subj.credits)
                num_credits += subj.credits
        return round(grades_x_credits / num_credits, 2)