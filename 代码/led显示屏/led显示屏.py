# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'led显示屏.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(826, 620)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 380, 381, 81))
        self.label.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 20pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(110, 460, 621, 121))
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 1000000000.0)
        self.lcdNumber.setProperty("intValue", 1000000000)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 381, 81))
        self.label_2.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 20pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2.setGeometry(QtCore.QRect(80, 110, 621, 121))
        self.lcdNumber_2.setSmallDecimalPoint(True)
        self.lcdNumber_2.setDigitCount(10)
        self.lcdNumber_2.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setProperty("value", 1000000000.0)
        self.lcdNumber_2.setProperty("intValue", 1000000000)
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "距离我们研究生毕业还有："))
        self.label_2.setText(_translate("Form", "现在的时间是："))

