from PyQt5 import QtWidgets

from StackedGUIS.SuppliesGui import SuppliesGui


class SuppliesFrame(QtWidgets.QFrame, SuppliesGui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)