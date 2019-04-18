# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '日历控件.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(708, 588)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(140, 140, 248, 197))
        self.calendarWidget.setObjectName("calendarWidget")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(160, 380, 194, 22))
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(390, 500, 118, 22))
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setObjectName("timeEdit")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(150, 430, 110, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(Form)
        self.calendarWidget.selectionChanged.connect(Form.show_date)
        self.dateTimeEdit.dateTimeChanged['QDateTime'].connect(Form.show_date_time)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dateTimeEdit.setDisplayFormat(_translate("Form", "yyyy 年 M 月 d 日 H:mm:ss"))
        self.timeEdit.setDisplayFormat(_translate("Form", "H:mm:ss"))

