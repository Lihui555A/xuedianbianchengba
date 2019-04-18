from 代码.转动按钮led显示数字.转动按钮led显示数字 import Ui_Form
from PyQt5.Qt import *
import sys
class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)


    def keyPressEvent(self, event):  #键盘按下事件
       self.label.setText(event.text())


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Mywin()
    win.show()
    sys.exit(app.exec_())
