# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '定时器总结.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(801, 509)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(114, 350, 111, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(244, 350, 121, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(394, 350, 121, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 350, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(43, 170, 151, 20))
        self.label.setStyleSheet("font: 75 14pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 170, 131, 20))
        self.label_2.setStyleSheet("font: 75 14pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(360, 170, 131, 20))
        self.label_3.setStyleSheet("font: 75 14pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(500, 170, 111, 20))
        self.label_4.setStyleSheet("font: 75 14pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "窗口本身定时器"))
        self.pushButton_2.setText(_translate("Form", "标签本身定时器"))
        self.pushButton_3.setText(_translate("Form", "系统定时器"))
        self.pushButton_4.setText(_translate("Form", "多线程"))
        self.label.setText(_translate("Form", "窗口本身定时器"))
        self.label_2.setText(_translate("Form", "标签本身定时器"))
        self.label_3.setText(_translate("Form", "系统定时器"))
        self.label_4.setText(_translate("Form", "多线程"))

