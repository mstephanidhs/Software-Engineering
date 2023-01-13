from PyQt5 import QtWidgets

from StackedGUIS.DashboardGui import DashboardGui


class DashboardFrame(QtWidgets.QFrame, DashboardGui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)