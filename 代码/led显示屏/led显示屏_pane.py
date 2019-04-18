from 代码.led显示屏.led显示屏 import Ui_Form
from PyQt5.Qt import *
import sys
import time
import datetime

class Mywin(QWidget, Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        #print(time.time())                                 #datetime是个模块，在这个模块里有几个常用的类，有datatime类，time类，date类等等
       # print(time.localtime())                            #最常用的是datetime类，在这个类中有today函数，表示此时此刻的日期和时间
        #print(time.ctime())                                #有now函数，返回的也是此时此刻的时间与日期
        #print(datetime.datetime.today())#
        #print(type(datetime.datetime.now()))
        #time1 = str(datetime.datetime.now())[:-7]
        #print(time1)
        self.lcdNumber.setDigitCount(20)
        self.lcdNumber_2.setDigitCount(20)
        time = str(datetime.datetime.now())[:-7]
        self.cross_time()
        self.lcdNumber_2.display(time)
        #设置显示的位数
        self.startTimer(1)
    def cross_time(self):
        startDate = QDateTime.currentMSecsSinceEpoch()
        endDate = QDateTime(QDate(2020, 3, 20), QTime(0, 0, 0)).toMSecsSinceEpoch()
        interval = endDate - startDate
        if interval > 0:
            days = interval // (24 * 60 * 60 * 1000)
            hour = (interval - days * 24 * 60 * 60 * 1000) // (60 * 60 * 1000)
            min = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000) // (60 * 1000)
            sec = (interval - days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000 - min * 60 * 1000) // 1000
            reasec=(interval- days * 24 * 60 * 60 * 1000 - hour * 60 * 60 * 1000 - min * 60 * 1000-sec*1000)
            if len(str(reasec))==3:
                intervals = str(days) + ':' + str(hour) + ':' + str(min) + ':' + str(sec)+':'+str(reasec)
                self.lcdNumber.display(intervals)
            elif len(str(reasec)) == 2:
                intervals = str(days) + ':' + str(hour) + ':' + str(min) + ':' + str(sec) + ': ' + str(reasec)
                self.lcdNumber.display(intervals)
            elif len(str(reasec)) == 1:
                intervals = str(days) + ':' + str(hour) + ':' + str(min) + ':' + str(sec) + ':  ' + str(reasec)
                self.lcdNumber.display(intervals)
    def timerEvent(self, event):
        time=str(datetime.datetime.now())[:-7]
        self.lcdNumber_2.display(time)
        self.cross_time()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Mywin()
    win.show()
    sys.exit(app.exec_())
