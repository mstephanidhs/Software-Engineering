import sys

from Login.loginUI import Ui_Form
from MainGUI.medicWorldGUI import Ui_MainGUI
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc



# Main class of the GUI that inherits the QWidget object and all its properties

class MainPage(qtw.QWidget):

    # Constructor method of the class
    def __init__(self):
        # call the constructor of the superclass QWidget
        super().__init__()

        # Create the instances of the UIs
        self.mainUI = Ui_MainGUI()
        self.loginUI = Ui_Form()

        # Initialize the login UIloginUI
        self.loginUI.setupUi(self)
        self.loginPage()

        self.show()

    # Method to connect all the signals of the Login Screen
    def loginPage(self):
        self.loginUI.loginbutton.clicked.connect(self.authenticate)

    # Method to make the authentication of the user for the login
    # will implement database authentication
    def authenticate(self):
        username = self.loginUI.username.text()
        password = self.loginUI.password.text()
        if username == "admin" and password == "admin":
            # for the purpose of this version after the credentials' username:admin password: admin
            # the app initializes the main GUI
            self.initMainPage()

    # Method to create the main GUI of the application
    def initMainPage(self):
        # Initialize the UI
        self.mainUI.setupUi(self)
        # Connect the stackedWidget in this case the left dashboard with the respective screens
        self.mainUI.listWidget.currentRowChanged.connect(self.display)
        self.mainUI.exitButton_2.clicked.connect(self.quitApp)
        # Init timers and datetimes
        self.startTimers()

    def startTimers(self):
        # Create a Qtimer object that updates every 1 sec and connect it with the method showTime()
        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

    # method that gets the current datetime for the top bar and the Dashboard screen
    def showTime(self):
        current_datetime = qtc.QDateTime.currentDateTime()
        topBarDateTime = current_datetime.toString("hh:mm:ss  dddd MMMM yy ")
        mainPageDate = current_datetime.toString("dddd dd, MMMM")
        self.mainUI.topDateTime_2.setText(topBarDateTime)
        self.mainUI.dateLabel.setText(mainPageDate)

    # method responsible to display the correct screen when  the user interacts with the left dashboard
    def display(self, i):
        self.mainUI.stackedWidget.setCurrentIndex(i)

    def quitApp(self):
        sys.exit()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainPage()
    app.exec_()
