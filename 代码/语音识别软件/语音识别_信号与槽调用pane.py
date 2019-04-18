
from 代码.语音识别软件.语音识别 import Ui_Form
from 代码.语音识别软件.语音识别_功能实现代码 import *
from PyQt5.Qt import *
import sys

class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.recognize_voice)
        self.thread=Mythread(self)
        signal.rest_time_singal.connect(self.show_rest_time)
        a.connect(self.show_result)
        self.pushButton_2.clicked.connect(self.set_write_time)
        self.write_time=40
    def show_result(self,str):
        self.textBrowser.setText(str)
    def recognize_voice(self):
        self.thread.start()
    def show_rest_time(self,int):
        self.label.setText('剩余语音时长：%d'%(int))
    def set_write_time(self):
        result,ok=QInputDialog.getInt(self,'设置时长','请输入时长')
        if ok:
            self.write_time=result
class Mythread(QThread):
    def __init__(self,window):
        super(Mythread, self).__init__(window)
        self.window=window
    def run(self):
        print(self.window.write_time)
        run(self.window.write_time)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Mywin()
    win.show()
    sys.exit(app.exec_())
