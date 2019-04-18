from 代码.设置限定格式的登录界面.限定格式的登录界面 import Ui_Form
from PyQt5.Qt import *
import sys
class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_password)

        regx = QRegExp("^[a-zA-Z][0-9A-Za-z]{14}$")
        validator = QRegExpValidator(regx, self.lineEdit)#三行解决验证器
        self.lineEdit.setValidator(validator)


        self.lineEdit.installEventFilter(self)  #给某个空间绑定一个事件过滤器
        object = QObject()
    def eventFilter(self, object, event):
        if object == self.lineEdit:
            if event.type() == QEvent.MouseMove or event.type() == QEvent.MouseButtonDblClick:
                return True
            elif event.type() == QEvent.KeyPress:
                key = QKeyEvent(event) #实例化一个键盘事件qqw
                if key.matches(QKeySequence.SelectAll) or key.matches(QKeySequence.Copy) or key.matches(
                        QKeySequence.Paste):
                    return True
        return QWidget.eventFilter(self, object, event)
    def get_password(self):
        text=self.lineEdit.text()
        if len(text) == 0:
            QMessageBox.warning(self, "警告", "密码为空")
        elif len(text) < 6:
            QMessageBox.warning(self, "警告", "密码长度低于6位")
        else:
            print(text)




if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Mywin()
    win.show()
    sys.exit(app.exec_())
