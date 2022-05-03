import sys

from Login.loginUI import Ui_Form
from MainGUI.medicWorldGUI import Ui_MainGUI
from PatientForm.newPatientGUI import Ui_NewPatient
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

        self.initMainPage()

        # Initialize the login UIloginUI
        # self.loginUI.setupUi(self)
        # self.loginPage()

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
        self.connectButtons()

    def connectButtons(self):
        self.loadSuppliesButtons()
        self.mainUI.newPatientButton.clicked.connect(self.openNewPatient)

    def openNewPatient(self):
        self.patientWindow = qtw.QMainWindow()
        self.patientFormGUI = Ui_NewPatient()
        self.patientFormGUI.setupUi(self.patientWindow)
        self.patientFormGUI.cancelPatientButon.clicked.connect(self.patientWindow.close)
        self.patientWindow.show()

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

    def loadSuppliesButtons(self):
        drugCategories = ["Analgesics", "Anticonvulsants", "Corticosteroids", "Antacids", "Antiemetics", "Laxatives", "Antiarrhythimcs", "Anti-Inflammatories",
                          "Sedatives", "Antibacterials", "Barbiturates", "Sleeping-Drugs", "Antibiotics", "Bronchodilators", "Tranquilizers" ]
        drugCol = [2,4,6]
        spacerCol = [1,3,5]
        self.SuppliesButtons = []
        drug =0
        for j in range(5):
            for i in range(3):
                hspacer = qtw.QSpacerItem(20, 10, qtw.QSizePolicy.Fixed)
                button =  qtw.QPushButton(drugCategories[drug])
                button.setStyleSheet("\n"
                                     "font-family: 'Roboto';\n"
                                     "font-style: normal;\n"
                                     "font-weight: 600;\n"
                                     "font-size: 32px;\n"
                                     "line-height: 38px;\n"
                                     "text-align: center;\n"
                                     "border: 0px;\n"
                                     "border-radius:10px;\n"
                                     "background: #FFFFFF;\n"
                                     "color: #1E2F97;\n"
                                     "\n")
                drug += 1
                button.setSizePolicy(qtw.QSizePolicy.Fixed,qtw.QSizePolicy.Fixed)
                button.setMinimumSize(330,108)
                self.mainUI.suppliesLayout.addItem(hspacer,j,spacerCol[i])
                self.mainUI.suppliesLayout.addWidget(button, j, drugCol[i] )


    # method responsible to display the correct screen when  the user interacts with the left dashboard
    def display(self, i):
        self.mainUI.stackedWidget.setCurrentIndex(i)

    def quitApp(self):
        sys.exit()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainPage()
    app.exec_()
