
from 代码.多选按钮.多选按钮 import Ui_Form
from PyQt5.Qt import *
import sys

class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.checkBox.stateChanged.connect(self.checkBox_change)
        self.checkBox_2.stateChanged.connect(self.checkBox_2_change)
        self.checkBox_3.stateChanged.connect(self.checkBox_2_change)
        self.checkBox_4.stateChanged.connect(self.checkBox_2_change)
        self.pushButton.clicked.connect(self.print_text)
    def checkBox_change(self):
        if self.checkBox.checkState()==Qt.Checked:
            self.checkBox_2.setChecked(True)  #设置选中
            self.checkBox_3.setChecked(True)
            self.checkBox_4.setChecked(True)
        elif self.checkBox.checkState()==Qt.Unchecked:
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_4.setChecked(False)
    def checkBox_2_change(self):
        if self.checkBox_2.isChecked() and self.checkBox_3.isChecked() and self.checkBox_4.isChecked():
            self.checkBox.setChecked(True)
        elif self.checkBox_2.isChecked() or self.checkBox_3.isChecked() or self.checkBox_4.isChecked():
            self.checkBox.setTristate(True)
            self.checkBox.setCheckState(Qt.PartiallyChecked)
        else:
            self.checkBox.setTristate(False)
            self.checkBox.setCheckState(Qt.Unchecked)
    def print_text(self):
        if self.checkBox.checkState()==Qt.Checked:
            print(self.checkBox_2.text()+self.checkBox_3.text()+self.checkBox_4.text())
        elif self.checkBox_2.isChecked()and self.checkBox_3.isChecked():
            print(self.checkBox_2.text()+self.checkBox_3.text())
        elif self.checkBox_2.isChecked()and self.checkBox_4.isChecked():
            print(self.checkBox_2.text()+self.checkBox_4.text())
        elif self.checkBox_3.isChecked()and self.checkBox_4.isChecked():
            print(self.checkBox_3.text()+self.checkBox_4.text())
        elif self.checkBox_2.isChecked():
            print(self.checkBox_2.text())
        elif self.checkBox_3.isChecked():
            print(self.checkBox_3.text())
        elif self.checkBox_4.isChecked():
            print(self.checkBox_4.text())
        else:
            print('貌似你没有勾选啊')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Mywin()
    win.show()
    sys.exit(app.exec_())
