from 代码.日历控件.日历控件 import Ui_Form
from PyQt5.Qt import *
import sys
import time
import datetime

class Mywin(QWidget, Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.startTimer(1000)
    def show_date(self):
        print(self.calendarWidget.selectedDate().toString(Qt.SystemLocaleLongDate))
        print(self.calendarWidget.selectedDate().toString('yyyy-MM-dd dddd'))
        print(self.calendarWidget.selectedDate().year(),self.calendarWidget.selectedDate().month(),self.calendarWidget.selectedDate().day(),)
    def show_date_time(self):
        pass
    def timerEvent(self, event):
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Mywin()
    win.show()
    sys.exit(app.exec_())
