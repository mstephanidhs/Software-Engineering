from PyQt5 import QtWidgets

from StackedGUIS.PatientScreenGui import PatientScreenGui


class PatientScreenFrame(QtWidgets.QFrame, PatientScreenGui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)