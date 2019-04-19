# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'label的使用.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(905, 664)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 60, 791, 41))
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(80, 130, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(80, 160, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(80, 190, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(53, 310, 111, 20))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 360, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 450, 101, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 500, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(730, 20, 151, 121))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(400, 30, 271, 71))
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 240, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(220, 150, 221, 331))
        self.label_6.setObjectName("label_6")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(780, 280, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(613, 390, 251, 191))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "点击下方单选按钮调整我的位置"))
        self.radioButton.setText(_translate("Form", "左边"))
        self.radioButton_2.setText(_translate("Form", "中间"))
        self.radioButton_3.setText(_translate("Form", "右边"))
        self.label_2.setText(_translate("Form", "我内容很少啊"))
        self.pushButton.setText(_translate("Form", "点我换内容"))
        self.label_3.setText(_translate("Form", "我内容很少啊"))
        self.pushButton_2.setText(_translate("Form", "点我换内容"))
        self.label_4.setText(_translate("Form", "小图片"))
        self.label_5.setText(_translate("Form", "大图片"))
        self.pushButton_3.setText(_translate("Form", "显示图片"))
        self.label_6.setText(_translate("Form", "动画"))
        self.pushButton_4.setText(_translate("Form", "播放动画"))
        self.label_7.setText(_translate("Form", "自动适应大小"))
