# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openfile_dialog_raw.ui'
#
# Created: Fri Jun  7 17:37:45 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_OpenFileDialog(object):
    def setupUi(self, OpenFileDialog):
        OpenFileDialog.setObjectName(_fromUtf8("OpenFileDialog"))
        OpenFileDialog.resize(430, 336)
        self.gridLayout = QtGui.QGridLayout(OpenFileDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_box = QtGui.QDialogButtonBox(OpenFileDialog)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Open)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.gridLayout.addWidget(self.button_box, 4, 0, 1, 2)
        self.file_path = QtGui.QLineEdit(OpenFileDialog)
        self.file_path.setObjectName(_fromUtf8("file_path"))
        self.gridLayout.addWidget(self.file_path, 1, 0, 1, 1)
        self.browse_button = QtGui.QPushButton(OpenFileDialog)
        self.browse_button.setObjectName(_fromUtf8("browse_button"))
        self.gridLayout.addWidget(self.browse_button, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 2)
        self.description = QtGui.QTextEdit(OpenFileDialog)
        self.description.setStyleSheet(_fromUtf8("background-color: transparent;"))
        self.description.setFrameShape(QtGui.QFrame.NoFrame)
        self.description.setObjectName(_fromUtf8("description"))
        self.gridLayout.addWidget(self.description, 0, 0, 1, 2)

        self.retranslateUi(OpenFileDialog)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), OpenFileDialog.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), OpenFileDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OpenFileDialog)
        OpenFileDialog.setTabOrder(self.browse_button, self.button_box)
        OpenFileDialog.setTabOrder(self.button_box, self.file_path)
        OpenFileDialog.setTabOrder(self.file_path, self.description)

    def retranslateUi(self, OpenFileDialog):
        OpenFileDialog.setWindowTitle(QtGui.QApplication.translate("OpenFileDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.browse_button.setText(QtGui.QApplication.translate("OpenFileDialog", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.description.setHtml(QtGui.QApplication.translate("OpenFileDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">Open File</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If you\'re concerned about entering your PSSO credentials in the program, there is an alternative, but it requires a few more steps from you.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Log in in PSSO the usual way through <a href=\"http://psso.fh-koeln.de\"><span style=\" text-decoration: underline; color:#0000ff;\">http://psso.fh-koeln.de</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Navigate to the page where you can see your grades</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Download the HTML page</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. Select the downloaded HTML page in the input field below</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

