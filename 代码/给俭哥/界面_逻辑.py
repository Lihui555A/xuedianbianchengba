from 代码.给俭哥.界面 import Ui_Form
from PyQt5.Qt import *
import sys
import cv2
class Mywin(QWidget, Ui_Form):
    def __init__(self):
        super(Mywin, self).__init__()
        self.setupUi(self)
        picture=QPixmap('1.jpg')
        self.label.setPixmap(picture)  #界面开始就有图片
        self.label.setScaledContents(True)  #让图片自适应标签大小，不然图片展示不全
        self.label_2.setScaledContents(True)#因为是两个展示图片的标签，所以都得设定
        self.pushButton.clicked.connect(self.chuli_picture)  #按钮连接下面的处理函数

    def partclahe_demo(self,image):
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))  # clipLimit可以改参数
        dst = clahe.apply(image)
        return dst

    #下面是你的处理方法
    def chuli_picture(self):
        img = cv2.imread('1.jpg') #这里我写死了，你可以看着改改
        b, g, r = cv2.split(img)
        bH = self.partclahe_demo(b)
        gH = self.partclahe_demo(g)
        rH = self.partclahe_demo(r)
        result = cv2.merge((bH, gH, rH))
        height, width = result.shape[:2]
        if result.ndim == 3:
            rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)  # 这里转换成rgb形式的，但是还是一堆数组
        temp_image = QImage(rgb.flatten(), width, height, QImage.Format_RGB888)
        temp_pixmap = QPixmap.fromImage(temp_image)
        self.label_2.setPixmap(temp_pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Mywin()
    win.show()
    sys.exit(app.exec_())
