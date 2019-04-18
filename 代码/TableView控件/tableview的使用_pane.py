from 代码.TableView控件.tableview的使用 import Ui_Form
from PyQt5.Qt import *
import sys
import time
import datetime
import random
class Mywin(QWidget, Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.model=QStandardItemModel(self)      #Tableviw继承自QAbstractItemView
        self.model.setHorizontalHeaderLabels(['标题1','标题2','标题3','标题4'])

        #设置选中模式
        #self.tableView.setSelectionMode(QAbstractItemView.NoSelection)  #不能选中
        #self.tableView.setSelectionMode(QAbstractItemView.ContiguousSelection) #只能选中一个
        #self.tableView.setSelectionMode(QAbstractItemView.MultiSelection) #可以多选
        #self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 按下control 多选多选
        #self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)#只能选择一个

        #设置选中模式
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectColumns) #全列选中
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  #全行选中
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)  #单个选中

        #设置背景是否用颜色交替
        print(self.tableView.alternatingRowColors())
        self.tableView.setAlternatingRowColors(True)
        print(self.tableView.alternatingRowColors())

        self.tableView.setEditTriggers(QAbstractItemView.SelectedClicked)#选择打开编辑的模式
        self.listview=QListView(self)
        self.listview.setViewMode()




        for row in range(10):
            for column in range(5):
                item=QStandardItem('row %s, column %s'%(row,column))
                self.model.setItem(row,column,item)
        self.tableView.setModel(self.model)
        self.pushButton.clicked.connect(self.func)

    def func(self):

        self.tableView.currentIndex() #取消选中的


if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Mywin()
    win.show()
    sys.exit(app.exec_())
