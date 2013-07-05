#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import codecs
import urllib
import re
import keyring

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL, SLOT

from login_dialog import LoginDialog
from donation_dialog import DonationDialog
from openfile_dialog import OpenFileDialog
from grades import GradesModel, GradesModelProxy
from checkbox_delegate import CheckBoxDelegate
from web_scraper import ParsingError, LoginError, ConnectionError
from web_scraper import ServiceUnavailableError
from main_window import MainWindow

VERSION = 0.9

class PSSOptimisation():
    def __init__(self):
        QtCore.QCoreApplication.setApplicationName("PSSOptimisation")
        QtCore.QCoreApplication.setApplicationVersion(str(VERSION))
        QtCore.QCoreApplication.setOrganizationName("Hubert Grzeskowiak")

        self.settings = QtCore.QSettings()
        self.main_window = MainWindow(True)
        self.grades_model = GradesModel(self.main_window)
        self.proxy_model = GradesModelProxy()
        self.proxy_model.setSourceModel(self.grades_model)
        self.initUI()
        tray = QtGui.QSystemTrayIcon(self.main_window)
        tray.setIcon(QtGui.QIcon("icons/Accessories-calculator.svg"))
        tray.connect(tray,
            SIGNAL("activated(QSystemTrayIcon::ActivationReason)"),
            self.trayClicked)
        tray.show()
        self.tray = tray

    def trayClicked(self, reason):
        print reason
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            self.main_window.setVisible(not self.main_window.isVisible())

    def initUI(self):
        self.connectUI()
        self.main_window.show()

    def connectUI(self):
        self.main_window.grades_table.setModel(self.proxy_model)
        delegate = CheckBoxDelegate()
        self.main_window.grades_table.setItemDelegate(delegate)

        self.main_window.connect(self.main_window.action_download,
            SIGNAL("triggered()"), self.openLoginDialog)
        self.main_window.connect(self.main_window.action_donate,
            SIGNAL("triggered()"), self.openDonationDialog)
        self.main_window.connect(self.main_window.action_open,
            SIGNAL("triggered()"), self.openFileDialog)
        self.main_window.connect(self.grades_model,
            SIGNAL("dataChanged()"), self.updateStats)
        self.main_window.connect(self.grades_model,
            SIGNAL("modelReset()"), self.updateStats)

        header = self.main_window.grades_table.horizontalHeader()
        #self.proxy_model.headerData(section, QtGui.Qt.Horizontal)
        self.header_actions = QtGui.QActionGroup(header)
        self.header_actions.setExclusive(False)
        for nr, (name, visible) in enumerate(zip(
            self.grades_model.header_data,
            self.proxy_model.col_visibility)):

            action = self.header_actions.addAction(name)
            action.setCheckable(True)
            action.setChecked(visible)
            action.connect(action, SIGNAL("triggered()"),
                lambda nr=nr: self.proxy_model.toggleColumn(nr))
        header.addActions(self.header_actions.actions())
        header.setContextMenuPolicy(
            QtCore.Qt.ActionsContextMenu)

        self.main_window.menu_table_columns.clear()
        for action in self.header_actions.actions():
            self.main_window.menu_table_columns.addAction(action)

        # automatically download new grades
        if self.settings.value("updateOnStart", False).toBool():
            QtCore.QTimer.singleShot(200, self.tryAutoDownloadFromPSSO)
    
    def openLoginDialog(self):
        self.login_dialog = LoginDialog(self.main_window)
        self.login_dialog.exec_()
        if self.login_dialog.result():
            username = str(self.login_dialog.username_line.text())
            password = str(self.login_dialog.password_line.text())
            if username and password:
                remember = self.login_dialog.remember_checkbox.isChecked()
                self.handleLoginData(username, password, remember)

    def handleLoginData(self, username, password, remember=False):
        """Try to load the grades by using the provided login credentials.
        On failure, an error popup is displayed. On success a loading progress
        bar and after that a table is shown.
        If "remember" is True, then the login data is saved.
        """
        self.main_window.setDisabled(True)
        QtGui.QApplication.processEvents()
        QtGui.QApplication.processEvents()
        progress = 0
        try:
            iterator = self.grades_model.getFromPSSOIterator(username, password)
            for step in iterator:
                self.main_window.showProgress(progress, step)
                # getFromPSSOIterator defines 8 steps, but 1st is at 0
                progress += 100.0/7
                QtGui.QApplication.processEvents()
        except (ConnectionError, ServiceUnavailableError, ParsingError) as e:
            QtGui.QMessageBox.critical(self.main_window,
                e.title, e.message)
            return
        except LoginError as e:
            self.clearLoginData(username)
            QtGui.QMessageBox.critical(self.main_window,
                e.title, e.message)
            return
        finally:
            self.main_window.setEnabled(True)
            self.main_window.showProgress(-1)
        self.main_window.showTable()
        self.main_window.grades_table.resizeColumnsToContents()
        self.main_window.grades_table.updateGeometries()

        self.main_window.setEnabled(True)
        if remember:
            self.saveLoginData(username, password)

    def saveLoginData(self, username, password):
        assert username and password
        self.settings.setValue("username", username)
        keyring.set_password("PSSO", username, password)

    def getLoginData(self):
        """Try to retrieve previously saved username and password. Returns
        a tuple of two empty strings on failure.
        """
        username = str(self.settings.value("username").toString() or "")
        try:
            password = keyring.get_password("PSSO", username) or ""
        except IOError:
            return "", ""
        return username, password

    def clearLoginData(self, username=None):
        """Remove username and password settings. If a username is given,
        its password will be removed. If there is a saved username,
        it will also get removed alongside with the corresponding password.
        """
        username2 = str(self.settings.value("username").toString() or "")
        try:
            keyring.delete_password("PSSO", username)
        except:
            pass
        try:
            keyring.delete_password("PSSO", username2)
        except:
            pass
        self.settings.remove("username")

    def tryAutoDownloadFromPSSO(self):
        u, p = self.getLoginData()
        if u and p:
            self.handleLoginData(u, p)

    def openFileDialog(self):
        ofd = OpenFileDialog(self.main_window)
        accepted = ofd.exec_()
        if accepted and ofd.html_file:
            try:
                html = codecs.open(ofd.html_file, encoding='utf-8')
            except IOError:
                QtGui.QMessageBox.warning(self.main_window, "File not found",
                    "Sorry, but there seems to be no file called {}.".format(
                        ofd.html_file))
                return
            self.grades_model.getFromHTML(html)
            self.main_window.showTable()
            self.main_window.grades_table.resizeColumnsToContents()
            self.main_window.grades_table.updateGeometries()

    def openDonationDialog(self):
        dp = DonationDialog(self.main_window)
        dp.exec_()

    def updateStats(self):
        self.main_window.num_of_grades.setText(str(
            self.grades_model.getNumOfGrades()))
        self.main_window.num_of_credits.setText(str(
            self.grades_model.getNumOfCredits()))
        self.main_window.average_grade.setText(str(
            self.grades_model.getAverageGrade()))

def main():
    app = QtGui.QApplication(sys.argv)

    translator = QtCore.QTranslator()
    translator.load("de.qm", ".")
    # enable
    app.installTranslator(translator)
    # disable
    app.removeTranslator(translator)

    ex = PSSOptimisation()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()