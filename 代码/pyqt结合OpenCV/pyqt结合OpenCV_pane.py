from 代码.pyqt结合OpenCV.pyqt结合OpenCV import Ui_Form
from PyQt5.Qt import *
import sys

class Mywin(QWidget, Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.label=Mylable(self)
        self.label.resize(300,300)

class Mylable(QLabel):
    def __init__(self,window):
        super(Mylable, self).__init__(window)
        self.x0=0
        self.y0=0
        self.x1=0
        self.y1=0
        self.window=window
        self.setPixmap(QPixmap('../小车快跑/image/000001.jpg'))

    def mousePressEvent(self, event):
       # self.flag=True
        self.x0=event.x()
        self.y0=event.y()
    def mouseMoveEvent(self, event):
        #if self.flag:
        self.x1=event.x()
        self.y1=event.y()
        self.update()
    def mouseReleaseEvent(self, event):
        pass
        #self.flag=False
    def paintEvent(self, event):
        super().paintEvent(event)
        painter=QPainter(self)
        rect=QRect(self.x0,self.y0,abs(self.x1-self.x0),abs(self.y1-self.y0))
        painter.setPen(QPen(Qt.black,4,Qt.SolidLine))
        painter.drawRect(rect)
        qpscreen=QGuiApplication.primaryScreen()
        pixmap2=qpscreen.grabWindow(self.winId(),rect.x(),rect.y(),rect.width(),rect.height())
        self.window.label_2.setPixmap(pixmap2)
        self.window.label_2.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Mywin()
    win.show()
    sys.exit(app.exec_())
