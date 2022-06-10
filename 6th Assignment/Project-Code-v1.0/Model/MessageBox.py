import PyQt5.QtWidgets as qtw

class MessageBox():

    def __init__(self, msg, title):

        if not isinstance(msg, str):
            raise TypeError(f"msg must be of <class 'str'> , {type(msg)} given")
        if not isinstance(title, str):
            raise TypeError(f"msg must be of <class 'str'> , {type(title)} given")
        self.message = msg
        self.title = title

    @property
    def messageGet(self):
        return self.message

    @property
    def titleGet(self):
        return self.title

    def createMessage(self):
        self.messageDialog = qtw.QMessageBox()
        self.messageDialog.setWindowTitle(self.titleGet)
        self.messageDialog.setIcon(qtw.QMessageBox.Critical)
        self.messageDialog.setText(self.messageGet)
        self.messageDialog.exec_()