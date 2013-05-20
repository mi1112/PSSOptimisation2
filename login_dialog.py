#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL, SLOT

from login_dialog_raw import Ui_LoginDialog

class LoginDialog(QtGui.QDialog, Ui_LoginDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent=parent)
        self.setupUi(self)

        # TODO: find out if caps lock is on and show this whenever necessary

        # Windows version:
        #from win32api import GetKeyState
        #from win32con import VK_CAPITAL
        #GetKeyState(VK_CAPITAL) # normal
        #GetKeyState(VK_CAPITAL) # CAPS LOCK set 1

        self.caps_warning.hide()

        # The showing and hiding from now on is handled by a connection
        # from the raw script. We only hide it at start because
        # the Qt Designer isn't able to.
        self.remember_warning.hide()
