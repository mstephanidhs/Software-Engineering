import sys,os


import  re
from PyQt5 import QtWidgets
from MainApp.DBPATH import DBPATH
from StackedGUIS.DrugFormGUI import Ui_Frame
from StackedGUIS.SuccessFrameGUI import  Ui_MainWindow
from Model.Drug import  Drug
from Model.ModelDB import ModelDB
from Model.MessageBox import MessageBox
from Frames.SuccessFrame import SuccessFrame

class NewDrugForm(QtWidgets.QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.editMap = {"category": self.medicationTypeEdit, "name":self.medicatonNameEdit,
                        "quantity": self.medicationQuantityEdit, "low": self.lowEdit, "mediocre": self.mediocreEdit,
                        "minimum": self.minimumEdit}
        self.buttonMapping()

    def buttonMapping(self):
        self.backButton.clicked.connect(self.clearALL)

    def doneChecker(self, connector):
        connector = ModelDB(DBPATH)
        drugNames = connector.selectData("select name from Medicine")
        drugNames = [x[0] for x in drugNames ]
        name = self.editMap["name"].text()
        quantities = self.editMap["quantity"].text()

        if Drug.drugExists(drugNames,name):
            popMessage = MessageBox("The drug you have inserted already exists", "Error")
            popMessage.createMessage()
            self.backButton.click()
            return

        if not Drug.quantitiesCheck(quantities):
            popMessage = MessageBox("Quantities invalid, please check again ", "Error")
            popMessage.createMessage()
            self.editMap["quantity"].clear()
            return



        if self.checkRequiredFields():
            drugCategories = connector.selectData("select distinct category from Medicine")
            drugCategories = [x[0] for x in drugCategories]
            if self.editMap["category"].text() not in drugCategories:
                popMessage = MessageBox("The Category you have written will be inserted into the system.", "Information")
                popMessage.createMessage()
            self.windowGUI = SuccessFrame(connector)
            self.windowGUI.setupUi(self.windowGUI)
            values = []
            for i in self.editMap.values():
                values.append(i.text())
            self.windowGUI.displaySuccessFrame(values)
            self.backButton.click()



    def checkRequiredFields(self):
        regexNumber = re.compile(r'[0-9]+')
        for edit in self.editMap.values():
            if len(edit.text()) == 0:
                popMessage = MessageBox("Please fill all the required fields!", "Error")
                popMessage.createMessage()
                return 0
        flagLow, flagMid, flagMin = "", "",""
        if not regexNumber.match(self.editMap["minimum"].text()):
            flagMin = "Minimum,"
            self.editMap["minimum"].clear()
        if not regexNumber.match(self.editMap["mediocre"].text()):
            flagMid = "Mediocre,"
            self.editMap["mediocre"].clear()
        if not regexNumber.match(self.editMap["low"].text()):
            flagLow = "Low"
            self.editMap["low"].clear()

        if flagLow or flagMid or flagMin:
            popMessage = MessageBox(f"Error in {flagMin}{flagMid}{flagLow}. Please check your fields","Error")
            popMessage.createMessage()
            return 0
        return 1


    def clearALL(self):
        for edit in self.editMap.values():
            edit.clear()
