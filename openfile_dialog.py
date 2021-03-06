#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL, SLOT

from openfile_dialog_raw import Ui_OpenFileDialog

class OpenFileDialog(QtGui.QDialog, Ui_OpenFileDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent=parent)
        self.setupUi(self)
        self.connectUI()
        self.skip_popup = False

    @property
    def html_file(self):
        return str(self.file_path.text())

    def connectUI(self):
        self.connect(self.browse_button, SIGNAL("clicked()"),
            self.chooseFile)

        def choseFileIfNonechosen(e):
            self.skip_popup = False
            if not str(self.file_path.text()) and not self.skip_popup:
                self.chooseFile()
                self.file_path.clearFocus()
            else:
                return QtGui.QLineEdit.focusInEvent(self.file_path, e)
        self.file_path.focusInEvent = choseFileIfNonechosen

    def chooseFile(self):
        html_file = QtGui.QFileDialog.getOpenFileName(None,
            u"Choose an HTML file", filter="HTML-Datei (*.html *.htm)")
        if html_file:
            self.file_path.setText(unicode(html_file))
        # if nothing was selected (e.g. form cancelled), prevent reopening
        self.skip_popup = not bool(html_file)
    