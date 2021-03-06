# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checklist.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ChecklistGui(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(1231, 871)
        Frame.setStyleSheet("background-color:#EEEEEE")
        self.roomsFrame = QtWidgets.QFrame(Frame)
        self.roomsFrame.setGeometry(QtCore.QRect(310, 170, 653, 165))
        self.roomsFrame.setStyleSheet("background:#FFFFFF;\n"
"border-radius:10px;")
        self.roomsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roomsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roomsFrame.setObjectName("roomsFrame")
        self.roomAvailability = QtWidgets.QLabel(self.roomsFrame)
        self.roomAvailability.setGeometry(QtCore.QRect(480, 30, 151, 41))
        self.roomAvailability.setStyleSheet("font-family:roboto-light;\n"
"font-size:18px;\n"
"color:#39FF14;\n"
"")
        self.roomAvailability.setObjectName("roomAvailability")
        self.roomsButton = QtWidgets.QPushButton(self.roomsFrame)
        self.roomsButton.setGeometry(QtCore.QRect(0, 0, 651, 161))
        self.roomsButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.roomsButton.setStyleSheet("text-align: left;\n"
"font-family:roboto;\n"
"font-size:32px;\n"
"color:#1E2F97;\n"
"font-weight:bold;")
        self.roomsButton.setFlat(True)
        self.roomsButton.setObjectName("roomsButton")
        self.label = QtWidgets.QLabel(self.roomsFrame)
        self.label.setGeometry(QtCore.QRect(540, 130, 101, 21))
        self.label.setStyleSheet("font-family:roboto-light;\n"
"font-size:16px;\n"
"font-weight:250")
        self.label.setObjectName("label")
        self.roomsButton.raise_()
        self.roomAvailability.raise_()
        self.label.raise_()
        self.laboratoriesFrame = QtWidgets.QFrame(Frame)
        self.laboratoriesFrame.setGeometry(QtCore.QRect(310, 411, 653, 165))
        self.laboratoriesFrame.setStyleSheet("background:#FFFFFF;\n"
"border-radius:10px;")
        self.laboratoriesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.laboratoriesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.laboratoriesFrame.setObjectName("laboratoriesFrame")
        self.laboratoriesButton = QtWidgets.QPushButton(self.laboratoriesFrame)
        self.laboratoriesButton.setGeometry(QtCore.QRect(0, 0, 651, 161))
        self.laboratoriesButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.laboratoriesButton.setStyleSheet("text-align: left;\n"
"font-family:roboto;\n"
"font-size:32px;\n"
"color:#1E2F97;\n"
"font-weight:bold;")
        self.laboratoriesButton.setFlat(True)
        self.laboratoriesButton.setObjectName("laboratoriesButton")
        self.labAvailability = QtWidgets.QLabel(self.laboratoriesFrame)
        self.labAvailability.setGeometry(QtCore.QRect(480, 30, 151, 41))
        self.labAvailability.setStyleSheet("font-family:roboto-light;\n"
"font-size:18px;\n"
"color:#39FF14;\n"
"")
        self.labAvailability.setObjectName("labAvailability")
        self.label_2 = QtWidgets.QLabel(self.laboratoriesFrame)
        self.label_2.setGeometry(QtCore.QRect(540, 130, 101, 21))
        self.label_2.setStyleSheet("font-family:roboto-light;\n"
"font-size:16px;\n"
"font-weight:250")
        self.label_2.setObjectName("label_2")
        self.orFrame = QtWidgets.QFrame(Frame)
        self.orFrame.setGeometry(QtCore.QRect(310, 651, 653, 165))
        self.orFrame.setStyleSheet("background:#FFFFFF;\n"
"border-radius:10px;")
        self.orFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.orFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.orFrame.setObjectName("orFrame")
        self.orButton = QtWidgets.QPushButton(self.orFrame)
        self.orButton.setGeometry(QtCore.QRect(-10, -10, 651, 161))
        self.orButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.orButton.setStyleSheet("text-align: left;\n"
"font-family:roboto;\n"
"font-size:32px;\n"
"color:#1E2F97;\n"
"font-weight:bold;")
        self.orButton.setFlat(True)
        self.orButton.setObjectName("orButton")
        self.orAvailability = QtWidgets.QLabel(self.orFrame)
        self.orAvailability.setGeometry(QtCore.QRect(480, 30, 151, 41))
        self.orAvailability.setStyleSheet("font-family:roboto-light;\n"
"font-size:18px;\n"
"color:#39FF14;\n"
"")
        self.orAvailability.setObjectName("orAvailability")
        self.label_3 = QtWidgets.QLabel(self.orFrame)
        self.label_3.setGeometry(QtCore.QRect(540, 130, 101, 21))
        self.label_3.setStyleSheet("font-family:roboto-light;\n"
"font-size:16px;\n"
"font-weight:250")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.roomAvailability.setText(_translate("Frame", "availability placeholder"))
        self.roomsButton.setText(_translate("Frame", "                   Rooms"))
        self.label.setText(_translate("Frame", "See more"))
        self.laboratoriesButton.setText(_translate("Frame", "               Laboratories"))
        self.labAvailability.setText(_translate("Frame", "availability placeholder"))
        self.label_2.setText(_translate("Frame", "See more"))
        self.orButton.setText(_translate("Frame", "                 Operating\n"
"                    Rooms"))
        self.orAvailability.setText(_translate("Frame", "availability placeholder"))
        self.label_3.setText(_translate("Frame", "See more"))

import MainGUI.resources