# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog_raw.ui'
#
# Created: Mon May 20 04:46:17 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName(_fromUtf8("LoginDialog"))
        LoginDialog.resize(374, 250)
        LoginDialog.setMinimumSize(QtCore.QSize(350, 250))
        LoginDialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(LoginDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 12, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setContentsMargins(3, 5, 3, -1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.username_label = QtGui.QLabel(LoginDialog)
        self.username_label.setObjectName(_fromUtf8("username_label"))
        self.gridLayout_2.addWidget(self.username_label, 0, 0, 1, 1)
        self.password_label = QtGui.QLabel(LoginDialog)
        self.password_label.setObjectName(_fromUtf8("password_label"))
        self.gridLayout_2.addWidget(self.password_label, 1, 0, 1, 1)
        self.username_line = QtGui.QLineEdit(LoginDialog)
        self.username_line.setObjectName(_fromUtf8("username_line"))
        self.gridLayout_2.addWidget(self.username_line, 0, 1, 1, 1)
        self.password_line = QtGui.QLineEdit(LoginDialog)
        self.password_line.setEchoMode(QtGui.QLineEdit.Password)
        self.password_line.setObjectName(_fromUtf8("password_line"))
        self.gridLayout_2.addWidget(self.password_line, 1, 1, 1, 1)
        self.caps_warning = QtGui.QLabel(LoginDialog)
        self.caps_warning.setObjectName(_fromUtf8("caps_warning"))
        self.gridLayout_2.addWidget(self.caps_warning, 2, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.login_msg = QtGui.QLabel(LoginDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_msg.sizePolicy().hasHeightForWidth())
        self.login_msg.setSizePolicy(sizePolicy)
        self.login_msg.setMargin(3)
        self.login_msg.setObjectName(_fromUtf8("login_msg"))
        self.gridLayout.addWidget(self.login_msg, 1, 0, 1, 1)
        self.remember_warning = QtGui.QLabel(LoginDialog)
        self.remember_warning.setWordWrap(True)
        self.remember_warning.setObjectName(_fromUtf8("remember_warning"))
        self.gridLayout.addWidget(self.remember_warning, 11, 0, 1, 1)
        self.button_box = QtGui.QDialogButtonBox(LoginDialog)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.gridLayout.addWidget(self.button_box, 13, 0, 1, 1)
        self.remember_checkbox = QtGui.QCheckBox(LoginDialog)
        self.remember_checkbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.remember_checkbox.setChecked(False)
        self.remember_checkbox.setObjectName(_fromUtf8("remember_checkbox"))
        self.gridLayout.addWidget(self.remember_checkbox, 6, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.username_label.setBuddy(self.username_line)
        self.password_label.setBuddy(self.password_line)

        self.retranslateUi(LoginDialog)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), LoginDialog.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), LoginDialog.reject)
        QtCore.QObject.connect(self.remember_checkbox, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.remember_warning.setVisible)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)
        LoginDialog.setTabOrder(self.username_line, self.password_line)
        LoginDialog.setTabOrder(self.password_line, self.button_box)

    def retranslateUi(self, LoginDialog):
        LoginDialog.setWindowTitle(QtGui.QApplication.translate("LoginDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.username_label.setText(QtGui.QApplication.translate("LoginDialog", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.password_label.setText(QtGui.QApplication.translate("LoginDialog", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.caps_warning.setText(QtGui.QApplication.translate("LoginDialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Caps Lock active!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.login_msg.setText(QtGui.QApplication.translate("LoginDialog", "Please enter your PSSO credentials below.", None, QtGui.QApplication.UnicodeUTF8))
        self.remember_warning.setText(QtGui.QApplication.translate("LoginDialog", "<html><head/><body><p><span style=\" font-weight:600; color:#ff0000;\">WARNING:</span> Your login data will be saved in plain text on your hard drive. This is a potential security leak.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.remember_checkbox.setText(QtGui.QApplication.translate("LoginDialog", "Remember me", None, QtGui.QApplication.UnicodeUTF8))

