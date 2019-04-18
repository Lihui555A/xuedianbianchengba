from 代码.工具按钮.工具按钮 import Ui_Form
from PyQt5.Qt import *
import sys
import time
import datetime

class Mywin(QWidget, Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        menu=QMenu(self)
        action_1=QAction(QIcon('../小车快跑/image/000001.jpg'),'支付宝',menu)
        action_1.triggered.connect(self.link_network)
        menu.addAction(action_1)
        self.toolButton_3.setPopupMode(QToolButton.MenuButtonPopup)  #这里是设置菜单的弹出模式，这样设置的话，下拉箭头在右中测，不这样设置下拉箭头在右下角
        self.toolButton_3.setMenu(menu)
        self.toolButton_2.setAutoRaise(True) #这句话是用来设置把按钮灰色背景给去掉的
        self.toolButton_3.setArrowType(Qt.UpArrow) #这个玩意是用来按钮箭头的，会把图标给盖掉的
    def link_network(self):
        QDesktopServices.openUrl(QUrl('https://www.alipay.com/'))
if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Mywin()
    win.show()
    sys.exit(app.exec_())
