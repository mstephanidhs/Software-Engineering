from PyQt5 import QtWidgets

from StackedGUIS.NewsroomGui import NewsroomGui


class NewsroomFrame(QtWidgets.QFrame, NewsroomGui):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)