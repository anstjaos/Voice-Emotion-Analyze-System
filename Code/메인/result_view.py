# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultview.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class ResultView(object):
    def __init__(self, Dialog):
        self.dialog = Dialog

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(654, 549)
        Dialog.setStyleSheet("background-color: rgb(209, 209, 209);")
        self.okBtn = QtWidgets.QPushButton(Dialog)
        self.okBtn.setGeometry(QtCore.QRect(134, 458, 121, 41))
        self.okBtn.setStyleSheet("background-color:rgb(52, 152, 219);\n"
"font: 75 10pt \"맑은 고딕\";\n"
"color: rgb(255, 255, 255);")
        self.okBtn.setObjectName("okBtn")
        self.okBtn.clicked.connect(self.closeResultView)
        self.saveBtn = QtWidgets.QPushButton(Dialog)
        self.saveBtn.setGeometry(QtCore.QRect(400, 458, 121, 41))
        self.saveBtn.setStyleSheet("background-color:rgb(52, 152, 219);\n"
"font: 75 10pt \"맑은 고딕\";\n"
"color: rgb(255, 255, 255);")
        self.saveBtn.setObjectName("saveBtn")
        self.imgLabel = QtWidgets.QLabel(Dialog)
        self.imgLabel.setGeometry(QtCore.QRect(370, 130, 221, 221))
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")
        self.resultLabel = QtWidgets.QLabel(Dialog)
        self.resultLabel.setGeometry(QtCore.QRect(50, 190, 271, 91))
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "결과 분석 창"))
        self.okBtn.setText(_translate("Dialog", "OK"))
        self.saveBtn.setText(_translate("Dialog", "분석 결과 저장"))
        self.resultLabel.setText(_translate("Dialog", "TextLabel"))

    def displayResultView(self):
        self.dialog.exec_()

    def closeResultView(self):
        self.dialog.close()

    def updateResultView(self, result):
        self.resultLabel.setText(result)
