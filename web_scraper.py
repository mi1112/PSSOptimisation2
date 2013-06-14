# encoding: utf-8
import sys
import urllib
import re
from datetime import datetime

from bs4 import BeautifulSoup

# TODO: translate
class ParsingError(Exception):
    def __init__(self, msg=("Outch. Looks like the PSSO has changed in a way"
        " that it makes this program not working anymore. Please contact the"
        " author about this.")):
        Exception.__init__(self, msg)
        self.title = "Parsing Error"

class LoginError(Exception):
    def __init__(self, msg=("Oops, are you sure your login data was correct?"
        " Please try again.")):
        Exception.__init__(self, msg)
        self.title = "Login Error"

class ConnectionError(Exception):
    def __init__(self, msg=("Sorry, fetching the html from PSSO not possible."
        " Maybe there's something wrong with your internet connection or"
        " the PSSO is not reachable at the moment.")):
        Exception.__init__(self, msg)
        self.title = "Connection Error"

class ServiceUnavailableError(Exception):
    def __init__(self, msg=("The PSSO service seems to be not available at"
        " the moment. Please check if the website is online and working."
        " Maybe you should try later.")):
        Exception.__init__(self, msg)
        self.title = "Service Unavailable"

# TODO: this method probably should rather be a class, since it yields
# progress but also returns a value. This being a class we might separate that.
def getHTMLFromPSSOIterator(username, password):
    """Return an HTML page with all grades in it.
    This function returns a generator that yields 6 strings that give info
    on the current progress and the grades html document as 7th value yielded.
    Use getHTMLFromPSSO() if you don't need the progress info.
    """
    login_url = ("https://psso.fh-koeln.de/qisserver/rds"
        "?state=user&type=1&category=auth.login&startpage=portal."
        "vm&breadCrumbSource=portal")
    params = urllib.urlencode({'asdf': username, 'fdsa': password,
        'submit':'Login'}) # lol at asdf and fdsa
    yield "Connecting to PSSO"
    try:
        html_1 = urllib.urlopen(login_url, params).read()
    except IOError:
        # Probably no internet connection
        raise ConnectionError()
    if checkServiceUnavailable(html_1):
        raise ServiceUnavailableError()
    yield "Checking login"
    if not checkLogin(html_1):
        raise LoginError()
    try:
        yield "Getting grades from PSSO (1/4)"
        html_2 = urllib.urlopen(
            getLinkByName(html_1, "Prüfungsverwaltung")).read()
        yield "Getting grades from PSSO (2/4)"
        html_3 = urllib.urlopen(
            getLinkByName(html_2, "Notenspiegel")).read()
        yield "Getting grades from PSSO (3/4)"
        html_4 = urllib.urlopen(
            getLinkByName(html_3, re.compile("Abschluss"))).read()
        yield "Getting grades from PSSO (4/4)"
        html_5 = urllib.urlopen(
            getLinkByGraphic(html_4, "/QIS/images//his_info3.gif")).read()
        yield html_5
    except TypeError as e:
        raise ParsingError()

def getHTMLFromPSSO(username, password):
    iterator = getHTMLFromPSSOIterator(username, password)
    for p in iterator:
        pass
    return p

def getSubjectsFromHTML(html):
    """Create a list of grades from an HTML page."""
    from grades import Subject
    soup = BeautifulSoup(html)
    # get the right table
    table = soup('table')[1]
    table = table.tbody or table
    rows = table.find_all("tr", recursive=False)
    # remove the table headers. we will use our own
    del rows[0]
    subjects = []
    for tr in rows:
        # all cells with real grades contain that css class.
        # skip all rows which first cell doesn't contain this.
        if tr.td["class"] != ["tabelle1_alignleft"]:
            continue
        tds = tr.find_all("td")
        # fill the text from the data cells into subjects
        subject = Subject(*([True]+[i.text.strip() for i in tds]))
        subject.grade = strToFloat(subject.grade) if subject.grade else None
        subject.credits = strToFloat(subject.credits) if subject.credits else None
        subject.date = strToDate(subject.date) if subject.date else None
        subjects.append(subject)
    return subjects

def getStudentName(html):
    soup = BeautifulSoup(html)
    return soup.find("table", summary=True).find("td").string

def checkLogin(html):
    """Check if the html indicates wrong login.
    If this function returns False, the login was wrong for sure.
    If it returns True, then either the login was right OR the given html
    simply didn't give any evidence of anything related.
    """
    soup = BeautifulSoup(html)
    fail_text = soup.find("font", text="Anmeldung fehlgeschlagen")
    return True if fail_text is None else False

def checkServiceUnavailable(html):
    """Check if the service is currently unavailable which is determined by
    checking the html title against "Service Unavailable".
    Returns True, if the service is unavailable for sure, else False.
    """
    soup = BeautifulSoup(html)
    return soup.title.string == "Service Unavailable"

def strToFloat(string):
    """Convert a string to float. European notation supported."""
    return float(string.strip().replace(',', '.'))

def strToDate(string):
    """Convert a string in form of dd.mm.yy into a python date object."""
    return datetime.strptime(string, "%d.%m.%Y").date()

def getLinkByName(html, name):
    soup = BeautifulSoup(html)
    return soup.find("a", text=name)["href"]

def getLinkByGraphic(html, img_src):
    soup = BeautifulSoup(html)
    for link in soup("a"):
        img = link.find("img", src=img_src)
        if img:
            return link["href"]

if __name__ == "__main__":
    main()