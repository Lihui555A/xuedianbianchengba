
import math
from 代码.重写鼠标与绘图事件.重写鼠标与绘图事件 import Ui_Form
from PyQt5.Qt import *
import sys

class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.label.adjustSize()
        self.mouse_place_x=0
        self.mouse_place_y = 0
        self.line_length=0
        self.setMouseTracking(True)
        sender = self.sender()

    def mouseMoveEvent(self,event):
        self.mouse_place_x=event.x()
        self.mouse_place_y=event.y()
        self.label.setText('鼠标当前位置为%d,%d,线的长度为%f'%(self.mouse_place_x,self.mouse_place_y,self.line_length))
        self.label.adjustSize()
        self.update()  #会调用下面这个painevent
    def paintEvent(self, event):
        paint=QPainter(self)
        paint.drawLine(0,0,self.mouse_place_x,self.mouse_place_y)
        self.line_length=math.sqrt(self.mouse_place_x*self.mouse_place_x+self.mouse_place_y*self.mouse_place_y)



if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Mywin()
    win.show()
    sys.exit(app.exec_())
