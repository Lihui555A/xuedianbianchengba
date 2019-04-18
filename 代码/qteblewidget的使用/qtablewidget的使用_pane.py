from tablewidget的使用 import Ui_Form
from PyQt5.Qt import *
import sys
import time
import datetime
import random
class Mywin(QWidget, Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.chose_picture)
        self.tableWidget.setColumnWidth(0,self.tableWidget.width())
        self.tableWidget.cellClicked.connect(self.print_row_column)  #这个能返回位置
        self.pushButton_2.clicked.connect(self.add_picture)

        self.tableWidget.hideColumn(1)
        self.tableWidget.setHorizontalHeaderLabels(['图片列表'])
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pushButton_3.clicked.connect(self.delete_picture)
    def chose_picture(self):
        imgName, imgType = QFileDialog.getOpenFileNames(self,"打开图片", "", " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        self.tableWidget.setRowCount(len(imgName))
        for index,picture_name in enumerate(imgName):
            lable=QLabel(self.tableWidget)
            item=QTableWidgetItem(picture_name)
            self.tableWidget.setRowHeight(index,100)
            lable.setObjectName(str(index))
            lable.setStyleSheet('QLabel#%s{border-image:url(%s)}'%(str(index),picture_name))

            # "QListWidget{border:1px solid gray; color:black; }"
            # "QListWidget::Item{padding-top:20px; padding-bottom:4px; }"
            # "QListWidget::Item:hover{background:skyblue; }"
            # "QListWidget::item:selected:!active{border-width:0px; background:lightgreen; }"


            self.tableWidget.setCellWidget(index,0,lable)
            self.tableWidget.setItem(index,1,item)


    def print_row_column(self,row,column):
        #print(row,column) #打印出点击的第一行第几列
        print(self.tableWidget.item(row,column+1).text())#这样就把每张图的绝对位置打出来了
        print(self.tableWidget.selectedItems())

        #self.tableWidget.item(row, column+1).setSelected(True)


        #self.tableWidget.clear() #全部删除但是表格还再
        #self.tableWidget.clearContents() #和上面的删除效果一样
       # print(self.tableWidget.column(item))#注意这里的item是要tablewidgetitem

        #print(self.tableWidget.currentColumn())#选中的当前列
        #print(self.tableWidget.currentRow())#选中的当前行
        #print(self.tableWidget.currentItem()) #选中的当前的item项目,没有返回none
    def add_picture(self):
        row_num=self.tableWidget.rowCount()  #拿出有几行
        imgName, imgType = QFileDialog.getOpenFileNames(self, "打开图片", "", " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        self.tableWidget.setRowCount(len(imgName)+row_num)
        for index, picture_name in enumerate(imgName):
            lable = QLabel(self.tableWidget)
            item = QTableWidgetItem(picture_name)
            self.tableWidget.setRowHeight(index+row_num, 100)
            lable.setObjectName('%s'%(str(index+row_num)))
            lable.setStyleSheet('QLabel#%s{border-image:url(%s)}'%(str(index+row_num),picture_name))
            self.tableWidget.setCellWidget(index+row_num,0,lable)
            self.tableWidget.setItem(index+row_num, 1, item)
    def delete_picture(self):
        print(self.tableWidget.removeRow(self.tableWidget.currentRow()))
        #print(self.tableWidget.selectedItems())
        picture_filepath_to_detect_list = []  #这里就把剩下的路径拿到手了
        for i in range(self.tableWidget.rowCount()):
            picture_filepath_to_detect_list.append(self.tableWidget.item(i, 1).text())
        print(picture_filepath_to_detect_list)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    win = Mywin()
    win.show()
    sys.exit(app.exec_())
