# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '爱不爱我.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(706, 568)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 170, 151, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 330, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = Mypushbutton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 320, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "你难道不爱我吗？"))
        self.pushButton.setText(_translate("Form", "爱"))
        self.pushButton_2.setText(_translate("Form", "不爱"))

from 代码.到底爱不爱我.爱不爱我_pane import Mypushbutton
