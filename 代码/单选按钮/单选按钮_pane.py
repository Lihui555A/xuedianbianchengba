
from 代码.单选按钮.单选按钮 import Ui_Form
from PyQt5.Qt import *
import sys

class Mywin(QWidget,Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.print_text)

    def print_text(self):
        if self.radioButton.isChecked() and self.radioButton_4.isChecked():
            print(self.radioButton.text()+self.radioButton_4.text())
        elif self.radioButton.isChecked() and self.radioButton_5.isChecked():
            print(self.radioButton.text() + self.radioButton_5.text())
        elif self.radioButton.isChecked() and self.radioButton_6.isChecked():
            print(self.radioButton.text() + self.radioButton_6.text())
        elif self.radioButton_2.isChecked() and self.radioButton_4.isChecked():
            print(self.radioButton_2.text() + self.radioButton_4.text())
        elif self.radioButton_2.isChecked() and self.radioButton_5.isChecked():
            print(self.radioButton_2.text() + self.radioButton_5.text())
        elif self.radioButton_2.isChecked() and self.radioButton_6.isChecked():
            print(self.radioButton_2.text() + self.radioButton_6.text())
        elif self.radioButton_3.isChecked() and self.radioButton_4.isChecked():
            print(self.radioButton_3.text() + self.radioButton_4.text())
        elif self.radioButton_3.isChecked() and self.radioButton_6.isChecked():
            print(self.radioButton_3.text() + self.radioButton_6.text())
        elif self.radioButton_3.isChecked() and self.radioButton_5.isChecked():
            print(self.radioButton_3.text() + self.radioButton_5.text())
        else:
            print('貌似你没有选吧')
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Mywin()
    win.show()
    sys.exit(app.exec_())
