from 代码.带菜单的按钮.带菜单的按钮 import Ui_Form
from PyQt5.Qt import *
import sys
import time
import datetime

class Mywin(QWidget, Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        menu=QMenu(self)
        action_1=QAction('我是大帅哥',menu)
        action_1.triggered.connect(lambda :print(action_1.text()))  #这样用来给菜单选项添加槽函数
        menu.addAction(action_1)
        menu.addAction(QAction('你是大傻叉',menu))
        menu.addAction(QAction('他是大英雄',menu))
        self.pushButton.setMenu(menu)
        self.pushButton_2.clicked.connect(self.send_password)
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.change_button_text)
        self.a=10
    def show_menu(self):
        pass
    def send_password(self):
        if self.pushButton_2.text() == '发送验证码':
            self.pushButton_2.setEnabled(False)
            self.timer.start(1000)
    def change_button_text(self):
        self.a-=1
        self.pushButton_2.setText('%s 秒后重发' % (str(self.a)))
        if self.a == 0:
            self.pushButton_2.setEnabled(True)
            self.pushButton_2.setText('发送验证码')
            self.timer.stop()
            self.a=10

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Mywin()
    win.show()
    sys.exit(app.exec_())
