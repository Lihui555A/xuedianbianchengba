# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '跑马灯.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(895, 717)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(160, 573, 631, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(True)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(Form)
        self.progressBar_2.setGeometry(QtCore.QRect(140, 150, 631, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(Form)
        self.progressBar_3.setGeometry(QtCore.QRect(140, 170, 20, 421))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_3.setInvertedAppearance(False)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_4 = QtWidgets.QProgressBar(Form)
        self.progressBar_4.setGeometry(QtCore.QRect(770, 150, 20, 421))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_4.setInvertedAppearance(True)
        self.progressBar_4.setObjectName("progressBar_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 630, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 630, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 630, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.progressBar_5 = QtWidgets.QProgressBar(Form)
        self.progressBar_5.setGeometry(QtCore.QRect(327, 260, 231, 23))
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setTextVisible(False)
        self.progressBar_5.setObjectName("progressBar_5")
        self.progressBar_6 = QtWidgets.QProgressBar(Form)
        self.progressBar_6.setGeometry(QtCore.QRect(330, 290, 231, 23))
        self.progressBar_6.setProperty("value", 24)
        self.progressBar_6.setTextVisible(False)
        self.progressBar_6.setInvertedAppearance(True)
        self.progressBar_6.setObjectName("progressBar_6")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 630, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "外同时"))
        self.pushButton_2.setText(_translate("Form", "外依次"))
        self.pushButton_3.setText(_translate("Form", "内外一起"))
        self.pushButton_4.setText(_translate("Form", "内部"))

