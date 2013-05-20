from PyQt4 import QtCore, QtGui

import web_scraper
from collections import namedtuple
from namedlist import namedlist

Subject = namedlist("Subject",
    ["nr", "name", "req", "exam_type", "semester", "grade",
    "status", "credits", "note", "attempt", "date"])

# TODO: translate
Subject.header = ["Nr", "Name", "Req", "Exam type", "Semester", "Grade",
    "Status", "Credits", "Note", "Attempt", "Date"]

class Grades(QtCore.QAbstractTableModel):
    def __init__(self, parent=None, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.headerdata = Subject.header
        self.subjects = []
        self.active = []

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
        # TODO: get this from settings
        self.active = [True] * len(subjects)
        self.endResetModel()
        yield "Done"
        # TODO: update number of rows

    def getFromPSSO(self, username, password):
        """Get grades from PSSO and feed them to the table model."""
        [x for x in self.getFromPSSOIterator(username, password)]

    def getFromHTML(self, html):
        subjects = web_scraper.getSubjectsFromHTML(html)
        self.beginResetModel()
        self.subjects = subjects
        self.active = [True] * len(subjects)
        self.endResetModel()
        # TODO: update number of rows

    def rowCount(self, parent):
    	return len(self.subjects)

    def columnCount(self, parent):
    	return len(self.headerdata) + 1

    def data(self, index, role):
        row, col = index.row(), index.column()
        if not index.isValid():
            return QtCore.QVariant()
        if role == QtCore.Qt.DisplayRole:
            if col == 0:
                return
            else:
                return self.subjects[row][col-1]
        elif role == QtCore.Qt.CheckStateRole:
            if col == 0:
                if self.active[row]:
                    return QtCore.Qt.Checked
                else:
                    return QtCore.Qt.Unchecked

    def headerData(self, index, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            if index == 0:
                return
            else:
                return self.headerdata[index-1]

    def flags(self, index):
        if index.column() == 0:
            return (QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
        else:
            return (QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
                #QtCore.Qt.ItemIsEditable)

    def setData(self, index, value, role):
        #if role == QtCore.Qt.EditRole:
            # TODO: make custom entries editable?
        #    pass
        if role == QtCore.Qt.CheckStateRole:
            row, col = index.row(), index.column()
            if col == 0:
                old = self.active[row]
                new = True if value == QtCore.Qt.Checked else False
                if old != new:
                    self.active[row] = new
                    


        return True