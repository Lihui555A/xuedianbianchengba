# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '工具按钮.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(728, 473)
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(60, 70, 91, 81))
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(220, 70, 141, 81))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolButton_2.setObjectName("toolButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 170, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 170, 81, 20))
        self.label_2.setObjectName("label_2")
        self.toolButton_3 = QtWidgets.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(400, 20, 131, 161))
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setIconSize(QtCore.QSize(81, 119))
        self.toolButton_3.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_3.setAutoRaise(True)
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(90, 230, 121, 121))
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setIconSize(QtCore.QSize(63, 78))
        self.toolButton_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_4.setObjectName("toolButton_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(420, 180, 91, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(90, 370, 101, 20))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "我是大双热"))
        self.toolButton_2.setText(_translate("Form", "..."))
        self.label.setText(_translate("Form", "只显示图标"))
        self.label_2.setText(_translate("Form", "只显示文字"))
        self.toolButton_3.setText(_translate("Form", "我\n"
"是\n"
"大\n"
"帅\n"
"哥\n"
""))
        self.toolButton_4.setText(_translate("Form", "我是大帅哥"))
        self.label_3.setText(_translate("Form", "文字在图标旁边"))
        self.label_4.setText(_translate("Form", "文字在图标下方"))

