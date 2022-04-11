import Dashboard.medicWorldGUI as ss
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc


class Test(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.UI =  ss.Ui_MainGUI()
        self.UI.setupUi(self)
        self.UI.listWidget.currentRowChanged.connect(self.display)


        self.show()

    def display(self, i):
        self.UI.stackedWidget.setCurrentIndex(i)


if __name__ == '__main__':
    app = qtw.QApplication([])
    mw = Test()
    app.exec_()

