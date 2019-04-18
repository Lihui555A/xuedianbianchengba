# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '转动按钮led显示数字.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(512, 417)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(120, 80, 231, 81))
        self.lcdNumber.setObjectName("lcdNumber")
        self.dial = QtWidgets.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(280, 200, 191, 111))
        self.dial.setObjectName("dial")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(60, 260, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(103, 360, 131, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.dial.valueChanged['int'].connect(self.lcdNumber.display)
        self.horizontalSlider.valueChanged['int'].connect(self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "按键盘我会变样子"))

