import PyQt5.QtWidgets as qtw
import sqlite3 as sql


class ModelDB():

    def __init__(self, dbName):
        self.dbName = dbName
        try:
            self.con = sql.connect(dbName)
            self.cursor = self.con.cursor()
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        except sql.Error as e:
            self.messageDialog = qtw.QMessageBox()
            self.messageDialog.setWindowTitle("Database Error")
            self.messageDialog.setIcon(qtw.QMessageBox.Critical)
            self.messageDialog.setText(str(e))
            self.messageDialog.exec_()
            print(e)

    def selectData(self, query):
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except sql.Error as e:
            self.messageDialog = qtw.QMessageBox()
            self.messageDialog.setWindowTitle("Database Error")
            self.messageDialog.setIcon(qtw.QMessageBox.Critical)
            self.messageDialog.setText(str(e))
            self.messageDialog.exec_()
            return False

    def storeData(self,query):

        try:
            self.cursor.execute(query)
            self.con.commit()
            return True
        except sql.Error as e:
            self.messageDialog = qtw.QMessageBox()
            self.messageDialog.setWindowTitle("Database Error")
            self.messageDialog.setIcon(qtw.QMessageBox.Critical)
            self.messageDialog.setText(str(e))
            self.messageDialog.exec_()
            return  False