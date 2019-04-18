
from 代码.设置进度对话框.设置进度对话框 import Ui_Form
from PyQt5.Qt import *
import sys

class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        validator = QIntValidator(self) #两行解决验证器
        self.lineEdit.setValidator(validator)
    def show_progress_dialog(self):
        num = int(self.lineEdit.text())
        progress = QProgressDialog(self)
        progress.setMinimumDuration(5)
        progress.setWindowModality(Qt.WindowModal)
        progress.setRange(0, num)
        for i in range(num):
            progress.setValue(i)
            if progress.wasCanceled():
                QMessageBox.warning(self,'提示','操作失败')
                break
        progress.setValue(num)





if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Mywin()
    win.show()
    sys.exit(app.exec_())
