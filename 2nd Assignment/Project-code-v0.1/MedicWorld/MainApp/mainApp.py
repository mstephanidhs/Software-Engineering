import sys

from Login.loginUI import Ui_Form
from MainGUI.medicWorldGUI import Ui_MainGUI
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc


class MainPage(qtw.QWidget):


    def __init__(self):
        super().__init__()
        # Create the instances of the UIs

        self.mainUI = Ui_MainGUI()
        self.loginUI = Ui_Form()

        # Initialize the login UIloginUI
        self.loginUI.setupUi(self)
        # Button mappings and signals for the login page
        self.loginPage()

        self.show()

    def loginPage(self):
        self.loginUI.loginbutton.clicked.connect(self.authenticate)

    def authenticate(self):
        username = self.loginUI.username.text()
        password = self.loginUI.password.text()
        if username == "admin" and password == "admin":
            self.initMainPage()

    def initMainPage(self):
        self.mainUI.setupUi(self)
        self.mainUI.listWidget.currentRowChanged.connect(self.display)
        # Init timers and datetimes
        self.startTimers()


    def startTimers(self):
        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

    def showTime(self):
        current_datetime = qtc.QDateTime.currentDateTime()
        test = current_datetime.toString("hh:mm:ss  dddd MMMM yy ")

    def display(self, i):
        self.mainUI.stackedWidget.setCurrentIndex(i)



    def quitApp(self):
        sys.exit()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainPage()
    app.exec_()
