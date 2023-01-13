from PyQt5 import QtWidgets

from StackedGUIS.SettingsGui import SettingsGui


class SettingsFrame(QtWidgets.QFrame, SettingsGui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)