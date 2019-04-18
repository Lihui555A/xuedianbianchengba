from 代码.到底爱不爱我.爱不爱我 import Ui_Form
from PyQt5.Qt import *
import sys
import time
import datetime
import random
class Mywin(QWidget, Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_picture)
    def show_picture(self):
        self.picture_window=QWidget(self)
        self.picture_window.resize(100,100)
        self.picture_window.move(100,100)


class Mypushbutton(QPushButton):
    def __init__(self,window):
        super(Mypushbutton, self).__init__(window)
        self.window=window
    def enterEvent(self, event):
        x=random.randint(0,self.window.width())
        y = random.randint(0, self.window.height())
        animation=QPropertyAnimation(self)
        animation.setTargetObject(self)
        animation.setPropertyName(b'pos')
        animation.setStartValue(self.pos())
        animation.setEndValue(QPoint(x,y))
        animation.setDuration(1)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Mywin()
    win.show()
    sys.exit(app.exec_())
