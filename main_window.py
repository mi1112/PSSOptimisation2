#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL, SLOT

from main_window_raw import Ui_PSSOptimisationMainWindow

class MainWindow(QtGui.QMainWindow, Ui_PSSOptimisationMainWindow):
    def __init__(self, first_start=True):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        # TODO: rethink the copy'n'paste stuff
        self.menu_edit.removeAction(self.action_copy)
        self.menu_edit.removeAction(self.action_paste)
        self.menu_edit.removeAction(self.action_cut)
        self.menu_edit.removeAction(self.action_select_all)

        self.setupShortcuts()
        self.setupStatusTips()
        self.setupProgressBar()

        if first_start:
            self.firstStart()
            self.center()
        else:
            self.showTable()

    def center(self):
        """Center the window on screen."""
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setupShortcuts(self):
        """Since the Qt Designer can't assign default shortcuts,
        we define them all here.
        """
        self.action_open.setShortcut(QtGui.QKeySequence.Open)
        self.action_download.setShortcut("Ctrl+D")
        self.action_donate.setShortcut("Ctrl+P")
        self.action_settings.setShortcut(QtGui.QKeySequence.Preferences)
        self.action_about.setShortcut(QtGui.QKeySequence.HelpContents)
        self.action_graph.setShortcut("Ctrl+G")
        self.action_quit.setShortcut(QtGui.QKeySequence.Quit)
        self.action_copy.setShortcut(QtGui.QKeySequence.Copy)
        self.action_cut.setShortcut(QtGui.QKeySequence.Cut)
        self.action_paste.setShortcut(QtGui.QKeySequence.Paste)
        self.action_select_all.setShortcut(QtGui.QKeySequence.SelectAll)

    def setupStatusTips(self):
        """Make tool tips also status tips that appear in the status bar."""
        for action in [self.action_open, self.action_download,
            self.action_donate, self.action_settings, self.action_about,
            self.action_graph, self.action_quit, self.action_copy,
            self.action_cut, self.action_paste, self.action_select_all]:

            action.setStatusTip(action.toolTip())

    def setupProgressBar(self):
        self.progressbar = QtGui.QProgressBar(self.status_bar)
        self.progressbar.setRange(0, 100)
        self.progressbar.hide()
        self.status_bar.addWidget(self.progressbar, 1)

    def firstStart(self):
        """Call this if the application is run for the first time and there is
        no saved data to show.
        """
        self.start_here.show()
        self.grades_table.hide()
        self.stats.hide()

    def showTable(self):
        """Call this when the table has been filled with data."""
        self.start_here.hide()
        self.grades_table.show()
        self.grades_table.resizeColumnsToContents()
        self.stats.show()

    def showGraph(self):
        pass

    def hideGraph(self):
        pass

    def showProgress(self, progress, text=""):
        """Shows progress in the status bar. progress param should be between 
        0 and 100 or -1, which makes the progress disappear.
        """
        if progress >= 0:
            self.progressbar.show()
            self.progressbar.setValue(progress)
            self.progressbar.setFormat(text)
            if progress >= 100:
                # Hide the progress bar after a second
                QtCore.QTimer.singleShot(1000, lambda: self.showProgress(-1))
        else:
            self.progressbar.reset()
            self.progressbar.hide()