from PyQt5 import QtWidgets

from StackedGUIS.ChecklistGui import ChecklistGui


class ChecklistFrame(QtWidgets.QFrame, ChecklistGui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
