
from 代码.跑马灯.跑马灯 import Ui_Form
from PyQt5.Qt import *
import sys
import time
class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.num=1000000
        self.progressBar.setRange(0,self.num)
        self.progressBar_2.setRange(0, self.num)
        self.progressBar_3.setRange(0, self.num)
        self.progressBar_4.setRange(0, self.num)
        self.progressBar_5.setRange(0, self.num)
        self.progressBar_6.setRange(0, self.num)
        self.pushButton.clicked.connect(self.same_time)
        self.pushButton_2.clicked.connect(self.no_same_time)
        self.pushButton_3.clicked.connect(self.start_time)
        self.pushButton_4.setText('开始')
        self.pushButton_4.clicked.connect(self.inner)
        self.lable=Mylabel(self,'nihao')
        self.woker=Mythread(self)

        self.lable.start()
    def same_time(self):
        for i in range(self.num):
            self.progressBar.setValue(i)
            self.progressBar_2.setValue(i)
            self.progressBar_3.setValue(i)
            self.progressBar_4.setValue(i)
    def no_same_time(self):
        for i in range(self.num+1):
            self.progressBar.setValue(i)
            if self.progressBar.value()==self.num-1:
                for i in range(self.num + 1):
                    self.progressBar_3.setValue(i)
                    if self.progressBar_3.value() == self.num - 1:
                        for i in range(self.num + 1):
                            self.progressBar_2.setValue(i)
                            if self.progressBar_2.value() == self.num - 1:
                                for i in range(self.num + 1):
                                    self.progressBar_4.setValue(i)
    def start_time(self):
        #self.woker.start(100,self)  #后边不一定是self 可以是别的控件，用来接收定时器事件
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(0)
        self.progressBar_2.setMinimum(0)
        self.progressBar_2.setMaximum(0)
        self.progressBar_3.setMinimum(0)
        self.progressBar_3.setMaximum(0)
        self.progressBar_4.setMinimum(0)
        self.progressBar_4.setMaximum(0)
    def timerEvent(self,event):
        value=self.progressBar_5.value()
        value+=1
        self.progressBar_5.setValue(value)
        self.lable.setText(str(value))
        self.lable.adjustSize()
    def inner(self):
        if self.pushButton_4.text()=='开始':
            self.id=self.startTimer(1000)
            self.woker.start()
            self.pushButton_4.setText('结束')
        elif self.pushButton_4.text()=='结束':
             self.killTimer(self.id)
             self.pushButton_4.setText('开始')

class Mylabel(QLabel):
    def __init__(self,window,value):
        super(Mylabel, self).__init__(window)
        self.window=window
        self.setText(value)
    def timerEvent(self,event):
        print(self.window.lable.text())
    def start(self):
        self.id=self.startTimer(1000)
    def stop(self):
        self.killTimer(self.id)
class Mythread(QThread):
    def __init__(self,window):
        super(Mythread, self).__init__(window)
        self.window=window
    def run(self):
        while True:
            print(self.window.lable.text())
            time.sleep(1)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Mywin()
    win.show()
    sys.exit(app.exec_())
