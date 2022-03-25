import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from loginscreen import Ui_MainWindow
import sys


class My_SuperduperWowzers_bazongersClass(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow();
        self.ui.setupUi(self)
        self.show()



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = My_SuperduperWowzers_bazongersClass()
    app.exec_()
