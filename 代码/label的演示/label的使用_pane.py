from 代码.label的演示.label的使用 import Ui_Form
from PyQt5.Qt import *
import sys
import time
import datetime

class Mywin(QWidget, Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.radioButton.clicked.connect(self.change_position)
        self.radioButton_2.clicked.connect(self.change_position)
        self.radioButton_3.clicked.connect(self.change_position)
        self.pushButton.clicked.connect(self.change_content)
        self.pushButton_2.clicked.connect(self.change_content)
        self.pushButton_3.clicked.connect(self.show_image)
        self.pushButton_4.clicked.connect(self.show_movie)
    def change_content(self):
        sender=self.sender()
        if sender==self.pushButton:
            result,ok=QInputDialog.getText(self,'获取内容','请输入想要改变的内容')
            if ok:
                self.label_2.setText(result)
        elif sender==self.pushButton_2:
            result,ok=QInputDialog.getText(self,'获取内容','亲输入想要的内容')
            if ok:
                self.label_3.setText(result)
    def show_movie(self):
        movie=QMovie('1.gif')
        self.label_6.setMovie(movie)
        self.label_6.setScaledContents(True)
        self.label_7.setMovie(movie)
        self.label_7.setScaledContents(True)

        movie.start()
        #如果想停止，movie.stop()

    def change_position(self):
        sender=self.sender()
        if sender==self.radioButton:
            self.label.setAlignment(Qt.AlignLeft)
        elif sender==self.radioButton_2:
            self.label.setAlignment(Qt.AlignCenter)
        else:
            self.label.setAlignment(Qt.AlignRight)

    def show_image(self):
        sender=self.sender()
        if sender==self.pushButton_3:
            self.label_4.setPixmap(QPixmap('../小车快跑/image/000001.jpg'))
            self.label_5.setPixmap(QPixmap('../小车快跑/image/000001.jpg'))
            self.label_5.setScaledContents(True)#这样话会使图片随着标签的大小自适应变化



if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Mywin()
    win.show()
    sys.exit(app.exec_())
