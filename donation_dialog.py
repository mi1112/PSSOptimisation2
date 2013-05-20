#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui

from donation_dialog_raw import Ui_DonationDialog

class DonationDialog(QtGui.QDialog, Ui_DonationDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent=parent)
        self.setupUi(self)