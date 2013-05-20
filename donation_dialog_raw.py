# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'donation_dialog_raw.ui'
#
# Created: Sun May 19 17:26:46 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DonationDialog(object):
    def setupUi(self, DonationDialog):
        DonationDialog.setObjectName(_fromUtf8("DonationDialog"))
        DonationDialog.resize(719, 449)
        self.verticalLayout = QtGui.QVBoxLayout(DonationDialog)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textEdit_2 = QtGui.QTextEdit(DonationDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMinimumSize(QtCore.QSize(290, 290))
        self.textEdit_2.setMaximumSize(QtCore.QSize(290, 290))
        self.textEdit_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.textEdit_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit_2.setUndoRedoEnabled(False)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.gridLayout_2.addWidget(self.textEdit_2, 3, 1, 1, 1)
        self.textEdit = QtGui.QTextEdit(DonationDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(300, 100))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.textEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_2.addWidget(self.textEdit, 0, 1, 1, 2)
        self.textBrowser_3 = QtGui.QTextBrowser(DonationDialog)
        self.textBrowser_3.setMinimumSize(QtCore.QSize(250, 200))
        self.textBrowser_3.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.textBrowser_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.textBrowser_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setUndoRedoEnabled(False)
        self.textBrowser_3.setReadOnly(True)
        self.textBrowser_3.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.textBrowser_3.setOpenExternalLinks(True)
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.gridLayout_2.addWidget(self.textBrowser_3, 3, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(DonationDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DonationDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DonationDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked(QAbstractButton*)")), DonationDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(DonationDialog)

    def retranslateUi(self, DonationDialog):
        DonationDialog.setWindowTitle(QtGui.QApplication.translate("DonationDialog", "Donate", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit_2.setHtml(QtGui.QApplication.translate("DonationDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/cookie-monster\" /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("DonationDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:xx-large; font-weight:600;\">Feed me!</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:18px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I develop this program in my spare time and don\'t get paid for it. If you like PSSOptimisation, consider donating a small tip. Thank you in advance!</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_3.setHtml(QtGui.QApplication.translate("DonationDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
"<tr>\n"
"<td style=\" vertical-align:middle; padding-right:10; padding-top:10; padding-bottom:20;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/cookie2\" height=\"20\" style=\"vertical-align: middle;\" /></p></td>\n"
"<td style=\" vertical-align:middle; padding-right:10; padding-top:10; padding-bottom:20;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Cookies are the preferred donation currency. </p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:middle; padding-right:10; padding-top:10; padding-bottom:20;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/bitcoin2\" height=\"20\" style=\"vertical-align: middle;\" /></p></td>\n"
"<td style=\" vertical-align:middle; padding-right:10; padding-top:10; padding-bottom:20;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Bitcoins at 1AV4wvZc5XuUNdxsyHg7sHMpd5GXoMJd26</p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:middle; padding-right:10; padding-top:10; padding-bottom:20;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://flattr.com/profile/hubertgrzeskowiak\"><img src=\":/icons/flattr2\" height=\"20\" style=\"vertical-align: middle;\" /></a></p></td>\n"
"<td style=\" vertical-align:middle; padding-right:10; padding-top:10; padding-bottom:20;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://flattr.com/profile/hubertgrzeskowiak\"><span style=\" text-decoration: underline; color:#0000ff;\">Flattr</span></a></p></td></tr>\n"
"<tr>\n"
"<td style=\" vertical-align:middle; padding-right:10; padding-top:10; padding-bottom:20;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=CDTWB6MUFK4G2\"><img src=\":/icons/paypal\" height=\"20\" style=\"vertical-align: middle;\" /></a></p></td>\n"
"<td style=\" vertical-align:middle; padding-right:10; padding-top:10; padding-bottom:20;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=CDTWB6MUFK4G2\"><span style=\" text-decoration: underline; color:#0000ff;\">paypal</span></a></p></td></tr></table></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
