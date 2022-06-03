from PyQt5 import QtWidgets

from StackedGUIS.MessagesGui import MessagesGui


class MessagesFrame(QtWidgets.QFrame, MessagesGui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)