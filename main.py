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
from grades import Grades
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
        self.grades = Grades(self.main_window)
        self.initUI()

    def initUI(self):
        self.connectUI()
        self.main_window.show()

    def connectUI(self):
        self.main_window.grades_table.setModel(self.grades)

        self.main_window.connect(self.main_window.action_download,
            SIGNAL("triggered()"), self.openLoginDialog)
        self.main_window.connect(self.main_window.action_donate,
            SIGNAL("triggered()"), self.openDonationDialog)
        self.main_window.connect(self.main_window.action_open,
            SIGNAL("triggered()"), self.openFileDialog)

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
        self.main_window.setDisabled(True)
        QtGui.QApplication.processEvents()
        QtGui.QApplication.processEvents()
        progress = 0
        try:
            iterator = self.grades.getFromPSSOIterator(username, password)
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
        html_file = QtGui.QFileDialog.getOpenFileName(None,
            u"Choose an HTML file", filter="HTML-Datei (*.html *.htm)")
        html_file = unicode(html_file)
        if html_file:
            html = codecs.open(html_file, encoding='utf-8')
            self.grades.getFromHTML(html)
            self.main_window.showTable()

    def openDonationDialog(self):
        dp = DonationDialog(self.main_window)
        dp.exec_()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = PSSOptimisation()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
