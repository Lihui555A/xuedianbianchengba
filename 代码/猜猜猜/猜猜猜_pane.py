from 代码.猜猜猜 import Ui_Form
from PyQt5.Qt import QWidget,QApplication,QMessageBox,QCloseEvent
import random
class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)  #后边这个self是指的空白窗体Qwidget
          # 产生随机数
    def show_message_box(self):
        self.num = random.randint(1, 100)
        guss_num=self.lineEdit.text()
        if int(guss_num)>self.num:
            QMessageBox.about(self,'提示框','你猜大了，正确答案为%d'%(self.num))
        elif int(guss_num)<self.num:
            QMessageBox.about(self,'提示框','你猜小了,正确答案为%d'%(self.num))
        else:
           QMessageBox.about(self,'提示框','你猜对了,进入下一轮')
           self.lineEdit.clear()
           self.lineEdit.setFocus()
    def closeEvent(self,event):                 #进函数的里边找参数类型，然后具体的类中找合适参数，然后看返回什么
        result=QMessageBox.question(self,'确认对话框','确实要关闭吗',QMessageBox.Yes | QMessageBox.No,QMessageBox.No) #返回的是个按钮控件
        if result==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    win_pane=Mywin()
    win_pane.show()


    sys.exit(app.exec_())




