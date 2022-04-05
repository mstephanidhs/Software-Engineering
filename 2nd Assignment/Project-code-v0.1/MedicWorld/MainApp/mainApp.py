import sys
from MainDoctorSreen.mainScreenUI import Ui_mainPage
from Login.loginUI import Ui_Form
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
import MainDoctorSreen.buttonStylesheets as bts


class MainPage(qtw.QWidget):
    DISABLED_BUTTON = None

    def __init__(self):
        super().__init__()
        # Create the instances of the UIs

        self.mainUI = Ui_mainPage()
        self.loginUI = Ui_Form()

        # Initialize the login UI
        self.loginUI.setupUi(self)
        # Button mappings and signals for the login page
        self.loginPage()

        # List for all the left footer buttons
        self.buttonList = None



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
        self.buttonList = [self.mainUI.dashboardButton, self.mainUI.patientsButton,
                           self.mainUI.checkListButton, self.mainUI.suppliesButton,
                           self.mainUI.newsroomButton, self.mainUI.settingButton]

        # Init timers and datetimes
        self.startTimers()

        self.dashboardClick()
        self.mainUI.dashboardButton.clicked.connect(self.dashboardClick)
        self.mainUI.patientsButton.clicked.connect(self.patientClick)
        self.mainUI.checkListButton.clicked.connect(self.checklistClick)
        self.mainUI.suppliesButton.clicked.connect(self.suppliesClick)
        self.mainUI.messagesButton.clicked.connect(self.messageClick)
        self.mainUI.newsroomButton.clicked.connect(self.newsroomClick)
        self.mainUI.settingButton.clicked.connect(self.settingsClick)

    def startTimers(self):
        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

    def showTime(self):
        current_datetime = qtc.QDateTime.currentDateTime()
        test = current_datetime.toString("hh:mm:ss  dddd MMMM yy ")
        self.mainUI.topDateTime.setText(test)
    def dashboardClick(self):
        self.turnBackButton()
        self.DISABLED_BUTTON = self.mainUI.dashboardButton
        self.mainUI.dashboardButton.setStyleSheet("QPushButton{\n image: url(:/img/img/home icon.png);\nborder:none;\n"
                                                  "font-size:20px;\n"
                                                  "font-family:Roboto;\n"
                                                  "color: #FFFFFF;\n"
                                                  "background-color: #7434A4;\n"
                                                  "}")
        self.mainUI.dashboardButton.setEnabled(False)

    def patientClick(self):
        self.turnBackButton()
        self.DISABLED_BUTTON = self.mainUI.patientsButton
        self.mainUI.patientsButton.setStyleSheet("QPushButton{\n image: url(:/img/img/users icon.png);\nborder:none;\n"
                                                 "font-size:20px;\n"
                                                 "font-family:Roboto;\n"
                                                 "color: #FFFFFF;\n"
                                                 "background-color: #7434A4;\n"
                                                 "}")
        self.mainUI.patientsButton.setEnabled(False)

    def checklistClick(self):
        self.turnBackButton()
        self.DISABLED_BUTTON = self.mainUI.checkListButton
        self.mainUI.checkListButton.setStyleSheet("QPushButton{\n image: url(:/img/img/check icon.png);\nborder:none;\n"
                                                  "font-size:20px;\n"
                                                  "font-family:Roboto;\n"
                                                  "color: #FFFFFF;\n"
                                                  "background-color: #7434A4;\n"
                                                  "}")
        self.mainUI.checkListButton.setEnabled(False)

    def suppliesClick(self):
        self.turnBackButton()
        self.DISABLED_BUTTON = self.mainUI.suppliesButton
        self.mainUI.suppliesButton.setStyleSheet(
            "QPushButton{\n image: url(:/img/img/pharmaceutical supplies.png);\nborder:none;\n"
            "font-size:20px;\n"
            "font-family:Roboto;\n"
            "color: #FFFFFF;\n"
            "background-color: #7434A4;\n"
            "}")
        self.mainUI.suppliesButton.setEnabled(False)

    def newsroomClick(self):
        self.turnBackButton()
        self.DISABLED_BUTTON = self.mainUI.newsroomButton
        self.mainUI.newsroomButton.setStyleSheet("QPushButton{\n image: url(:/img/img/pngkey 1.png);\nborder:none;\n"
                                                 "font-size:20px;\n"
                                                 "font-family:Roboto;\n"
                                                 "color: #FFFFFF;\n"
                                                 "background-color: #7434A4;\n"
                                                 "}")
        self.mainUI.newsroomButton.setEnabled(False)

    def messageClick(self):
        self.turnBackButton()
        self.DISABLED_BUTTON = self.mainUI.messagesButton
        self.mainUI.messagesButton.setStyleSheet(
            "QPushButton{\n image: url(:/img/img/envelope vector.png);\nborder:none;\n"
            "font-size:20px;\n"
            "font-family:Roboto;\n"
            "color: #FFFFFF;\n"
            "background-color: #7434A4;\n"
            "}")
        self.mainUI.messagesButton.setEnabled(False)

    def settingsClick(self):
        self.turnBackButton()
        self.DISABLED_BUTTON = self.mainUI.settingButton
        self.mainUI.settingButton.setStyleSheet(
            "QPushButton{\n image: url(:/img/img/gear icon.png);\nborder:none;\n"
            "font-size:20px;\n"
            "font-family:Roboto;\n"
            "color: #FFFFFF;\n"
            "background-color: #7434A4;\n"
            "}")
        self.mainUI.settingButton.setEnabled(False)

    def turnBackButton(self):
        if self.DISABLED_BUTTON:
            self.buttonChooser(self.DISABLED_BUTTON.text().strip())
            self.DISABLED_BUTTON.setEnabled(True)

    def buttonChooser(self, name):
        match name:
            case "Dashboard":
                self.mainUI.dashboardButton.setStyleSheet("QPushButton{\n"
                                                          "   image: url(:/img/img/home icon.png);\n"
                                                          "\n"
                                                          "border:none;\n"
                                                          "font-size:20px;\n"
                                                          "font-family:Roboto;\n"
                                                          "color: #FFFFFF;\n"
                                                          "background-color: #152238;\n"
                                                          "}\n")
            case "Patients":
                self.mainUI.patientsButton.setStyleSheet("QPushButton{\n"
                                                         
                                                         "   image: url(:/img/img/users icon.png);\n"
                                                         "\n"
                                                         "border:none;\n"
                                                         "font-size:20px;\n"
                                                         "font-family:Roboto;\n"
                                                         "color: #FFFFFF;\n"
                                                         "background-color: #152238;\n"
                                                         "}\n")
            case "Checklist":
                self.mainUI.checkListButton.setStyleSheet("QPushButton{\n"
                                                          "   image: url(:/img/img/check icon.png);\n"
                                                          "\n"
                                                          "border:none;\n"
                                                          "font-size:20px;\n"
                                                          "font-family:Roboto;\n"
                                                          "color: #FFFFFF;\n"
                                                          "background-color: #152238;\n"
                                                          "}\n")
            case "Supplies":
                self.mainUI.suppliesButton.setStyleSheet("QPushButton{\n"
                                                         "   image: url(:/img/img/pharmaceutical supplies.png);\n"
                                                         "\n"
                                                         "border:none;\n"
                                                         "font-size:20px;\n"
                                                         "font-family:Roboto;\n"
                                                         "color: #FFFFFF;\n"
                                                         "background-color: #152238;\n"
                                                         "}\n")
            case "Messages":
                self.mainUI.messagesButton.setStyleSheet("QPushButton{\n"
                                                         "   image: url(:/img/img/envelope vector.png);\n"
                                                         "\n"
                                                         "border:none;\n"
                                                         "font-size:20px;\n"
                                                         "font-family:Roboto;\n"
                                                         "color: #FFFFFF;\n"
                                                         "background-color: #152238;\n"
                                                         "}\n")
            case "Newsroom":
                self.mainUI.newsroomButton.setStyleSheet("QPushButton{\n"
                                                         "   image: url(:/img/img/pngkey 1.png);\n"
                                                         "\n"
                                                         "border:none;\n"
                                                         "font-size:20px;\n"
                                                         "font-family:Roboto;\n"
                                                         "color: #FFFFFF;\n"
                                                         "background-color: #152238;\n"
                                                         "}\n")
            case "Settings":
                self.mainUI.settingButton.setStyleSheet("QPushButton{\n"
                                                        "   image: url(:/img/img/gear icon.png);\n"
                                                        "\n"
                                                        "border:none;\n"
                                                        "font-size:20px;\n"
                                                        "font-family:Roboto;\n"
                                                        "color: #FFFFFF;\n"
                                                        "background-color: #152238;\n"
                                                        "}\n")

    def quitApp(self):
        sys.exit()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainPage()
    app.exec_()
