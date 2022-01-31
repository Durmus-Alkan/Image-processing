import cv2
import imutils
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QFileDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 640)
        self.btn1 = QtWidgets.QPushButton(Dialog)
        self.btn1.setGeometry(QtCore.QRect(120, 120, 251, 161))
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(Dialog)
        self.btn2.setGeometry(QtCore.QRect(390, 120, 251, 161))
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(Dialog)
        self.btn3.setGeometry(QtCore.QRect(120, 290, 251, 161))
        self.btn3.setObjectName("btn3")
        self.btn4 = QtWidgets.QPushButton(Dialog)
        self.btn4.setGeometry(QtCore.QRect(390, 290, 251, 161))
        self.btn4.setObjectName("btn4")
        self.gozat = QtWidgets.QPushButton(Dialog)
        self.gozat.setGeometry(QtCore.QRect(340, 480, 93, 28))
        self.gozat.setObjectName("gozat")
        self.resim = QtWidgets.QLabel(Dialog)
        self.resim.setGeometry(QtCore.QRect(650, 100, 400, 400))
        self.resim.setText("")
        self.resim.setObjectName("resim")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 90, 161, 16))
        self.label.setObjectName("label")
        self.tEditKernel = QtWidgets.QTextEdit(Dialog)
        self.tEditKernel.setGeometry(QtCore.QRect(300, 80, 91, 31))
        self.tEditKernel.setObjectName("tEditKernel")
        self.tEditKernel.setText("5")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #Tıklama olayları
        self.btn1.clicked.connect(self.agirlikli_ortalama_yumusatmasi)
        self.btn3.clicked.connect(self.median_yumusatmasi)
        self.btn2.clicked.connect(self.gaus_yumusatmasi)
        self.btn4.clicked.connect(self.bilateral_yumusatma)
        self.gozat.clicked.connect(self.gozat1)


    def gozat1(self):
        print("Button pressed")
        self.open_dialog_box()


    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        global path
        path = filename[0]



    def kernel_secme(self):
        global path
        img = cv2.imread(path)
        kernel = np.ones((16, 16), np.float32) / 25
        dst = cv2.filter2D(img, 1, kernel)

    def agirlikli_ortalama_yumusatmasi(self):
        global path

        img = cv2.imread(path)
        box = cv2.boxFilter(img, -1, (16, 16))
        gImage = imutils.resize(box, width=400, height=400)
        frame = cv2.cvtColor(gImage, cv2.COLOR_BGR2RGB)
        gImage = QImage(
            frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.resim.setPixmap(QtGui.QPixmap.fromImage(gImage))


    def gaus_yumusatmasi(self):
        global path
        img = cv2.imread(path)
        gblur = cv2.GaussianBlur(img, (11, 11), 150)
        gImage = imutils.resize(gblur, width=400, height=400)
        frame = cv2.cvtColor(gImage, cv2.COLOR_BGR2RGB)
        gImage = QImage(
            frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.resim.setPixmap(QtGui.QPixmap.fromImage(gImage))

    def median_yumusatmasi(self):
        global path
        img = cv2.imread(path)
        mblur = cv2.medianBlur(img, 5)
        gImage = imutils.resize(mblur, width=400, height=400)
        frame = cv2.cvtColor(gImage, cv2.COLOR_BGR2RGB)
        gImage = QImage(
            frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.resim.setPixmap(QtGui.QPixmap.fromImage(gImage))

    def bilateral_yumusatma(self):
        global path
        img = cv2.imread(path)
        bblur = cv2.bilateralFilter(img, 11, 40, 40)
        gImage = imutils.resize(bblur, width=400, height=400)
        frame = cv2.cvtColor(gImage, cv2.COLOR_BGR2RGB)
        gImage = QImage(
            frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.resim.setPixmap(QtGui.QPixmap.fromImage(gImage))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn1.setText(_translate("Dialog", "Ağırlıklı Ortalama Yumuşatması"))
        self.btn2.setText(_translate("Dialog", "Gauss Yumuşatması"))
        self.btn3.setText(_translate("Dialog", "Median Yumuşatması"))
        self.btn4.setText(_translate("Dialog", "Bilateral Yumuşatma"))
        self.gozat.setText(_translate("Dialog", "Gözat"))
        self.label.setText(_translate("Dialog", "Kernel Boyutunu Giriniz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
