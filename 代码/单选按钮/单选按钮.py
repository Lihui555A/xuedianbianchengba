# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '单选按钮.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 110, 120, 80))
        self.widget.setObjectName("widget")
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 30, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 10, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(20, 50, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(180, 110, 120, 91))
        self.widget_2.setObjectName("widget_2")
        self.radioButton_6 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 20, 89, 16))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 40, 89, 16))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget_2)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 0, 89, 16))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton_3.setText(_translate("Form", "你是"))
        self.radioButton_2.setText(_translate("Form", "我是"))
        self.radioButton.setText(_translate("Form", "他是"))
        self.radioButton_6.setText(_translate("Form", "美女"))
        self.radioButton_5.setText(_translate("Form", "傻叉"))
        self.radioButton_4.setText(_translate("Form", "帅哥"))
        self.pushButton.setText(_translate("Form", "打印"))

