from PyQt5 import QtWidgets

from StackedGUIS.SuccessFrameGUI import Ui_MainWindow
from Model.Drug import Drug


class SuccessFrame(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, connector,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connector = connector
        self.show()


    def displaySuccessFrame(self, values):
        self.values = values
        self.categoryLabel.setText(self.values[0])
        self.nameLabel.setText(self.values[1])
        self.quantityLabel.setText(self.values[2])
        self.minimumLabel.setText(self.values[3])
        self.mediocreLabel.setText(self.values[4])
        self.lowLabel.setText(self.values[5])
        self.confirmButton.clicked.connect(self.confirm)

    def confirm(self):
        cat, name, quan, minn, med, low = self.values
        newDrug = Drug(cat, name, quan, minn, med, low)
        newDrug.store(self.connector)
        self.close()