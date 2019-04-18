
from 代码.定时器总结.定时器总结 import Ui_Form
from PyQt5.Qt import *
import sys
import time
import random
class Mylabel(QLabel):
    def __init__(self,window):
        super(Mylabel, self).__init__(window)
    def timerEvent(self, event):
        colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = ""

        for i in range(6):
            color += colorArr[random.randint(0, 14)]
        self.setStyleSheet('QLabel{color:%s;font: 75 14pt "微软雅黑";}' % ('#' + color))
        self.adjustSize()

    def start(self):

        self.id=self.startTimer(100)

    def stop(self):
        self.killTimer(self.id)

class Mythread(QThread):
    def __init__(self,window):
        super(Mythread, self).__init__(window)
        self.window=window
    def run(self):
        while True:
            colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            color = ""

            for i in range(6):
                color += colorArr[random.randint(0, 14)]
            self.window.label_4.setStyleSheet('QLabel{color:%s;font: 75 14pt "微软雅黑";}' % ('#' + color))
            time.sleep(0.1)




class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.label_2=Mylabel(self)
        self.label_2.setText('标签本身定时器')
        self.label_2.setGeometry(QRect(200, 170, 131, 20))
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change)
        self.worker=Mythread(self)

        self.pushButton.clicked.connect(self.change_label_1_color)
        self.pushButton_2.clicked.connect(self.change_label_2_color)
        self.pushButton_3.clicked.connect(self.change_label_3_color)
        self.pushButton_4.clicked.connect(self.change_label_4_color)



    def timerEvent(self,event):
        colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = ""
        for i in range(6):
            color += colorArr[random.randint(0, 14)]
        self.label.setStyleSheet('QLabel#label{color:%s;font: 75 14pt "微软雅黑";}' % ('#' + color))
    def change_label_1_color(self):
        if self.pushButton.text()=='窗口本身定时器':
            self.id=self.startTimer(100)
            self.pushButton.setText('停止')
        else:
            self.killTimer(self.id)
            self.pushButton.setText('窗口本身定时器')




    def change_label_2_color(self):
        if self.pushButton_2.text()=='标签本身定时器':
            self.label_2.start()
            self.pushButton_2.setText('停止')

        else:
            self.label_2.stop()
            self.pushButton_2.setText('标签本身定时器')


    def change_label_3_color(self):
        if self.pushButton_3.text()=='系统定时器':
            self.timer.start(100)
            self.pushButton_3.setText('停止')
        else:
            self.timer.stop()
            self.pushButton_3.setText('系统定时器')
    def change(self):
        colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = ""
        for i in range(6):
            color += colorArr[random.randint(0, 14)]
        self.label_3.setStyleSheet('QLabel#label_3{color:%s;font: 75 14pt "微软雅黑";}' % ('#' + color))



    def change_label_4_color(self):
        if self.pushButton_4.text()=='多线程':
            self.worker.start()
            self.pushButton_4.setText('停止')

class Mytimer(QTimer):
    def __init__(self):
        super(Mytimer, self).__init__()


        
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Mywin()
    win.show()
    sys.exit(app.exec_())
