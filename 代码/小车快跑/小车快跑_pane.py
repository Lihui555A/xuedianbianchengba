
from 代码.小车快跑.小车快跑 import Ui_Form
from PyQt5.Qt import *
import sys

class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.horizontalSlider.valueChanged.connect(self.change_label_value)
        self.label_3.setText('')
        self.label_3.setPixmap(QPixmap('./image/000001.jpg'))
    def change_label_value(self,value):
        if 0<value<=9:
            self.label_3.setPixmap(QPixmap('./image/00000%s.jpg'%(value)))
        elif 10<=value<=99:
            self.label_3.setPixmap(QPixmap('./image/0000%s.jpg' % (value)))
        else:
            self.label_3.setPixmap(QPixmap('./image/000001.jpg'))
        self.label.setText('滑块当前值: %s'%(value))
        self.label_2.setText('滑块当前值: %s' % (value))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Mywin()
    win.show()
    sys.exit(app.exec_())
