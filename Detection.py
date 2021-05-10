# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Face Recognition\Upload.ui'
#
# Created by: PyQt5 UI code generator 5.15.4

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PIL.ImageQt import ImageQt
from FER_Image import detection_FER
import sys
from PIL import Image
from resizeimage import resizeimage


class Ui_Detection(object):
    def clear(self):
        self.lineEdit.clear()
        self.image.clear()
        self.expression.clear()
    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def browse_file(self):
        fileName,_= QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "*")
        print(fileName)
        self.lineEdit.setText(fileName)

    def detction(self):
        try:
            testimage = self.lineEdit.text()
            emotion_text = detection_FER(testimage)
            with open('..\FER_CNN\\result.jpg', 'r+b') as f:
                with Image.open(f) as image:
                    cover = resizeimage.resize_cover(image, [350, 350])
                    cover.save('..\FER_CNN\output.jpg', image.format)
            img = QPixmap('..\FER_CNN\output.jpg')
            self.image.setPixmap(img)
            self.expression.setText(emotion_text)


        except Exception as e:
            print("Error=" + e.args[1])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 650)
        Dialog.setStyleSheet("QDialog{background-image: url(../FER_CNN/Images/black.jpg);}")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 560, 321, 51))
        self.label_2.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n""color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.expression = QtWidgets.QLabel(Dialog)
        self.expression.setGeometry(QtCore.QRect(300, 560, 321, 51))
        self.expression.setStyleSheet("font: 24pt \"MS Shell Dlg 2\";\n"
                                   "color: rgb(0, 255, 255);")
        self.expression.setAlignment(QtCore.Qt.AlignCenter)
        self.expression.setObjectName("expression")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(163, 264, 71, 71))
        #self.label_3.setStyleSheet("background-image: url(../FER_CNN/Images/uploadimg.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.image = QtWidgets.QLabel(Dialog)
        self.image.setGeometry(QtCore.QRect(27, 130, 350, 350))
        self.image.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(168, 168, 168, 45), stop:1 rgba(255, 255, 255, 255));")
        self.image.setFrameShape(QtWidgets.QFrame.Box)
        self.image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.image.setLineWidth(2)
        self.image.setText("")
        self.image.setObjectName("image")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(409, 321, 451, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(389, 286, 211, 31))
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(733, 324, 121, 33))
        self.pushButton.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 370, 151, 41))
        self.pushButton_2.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 370, 151, 41))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("font: 12pt \"\";\n"
                                        "font: 63 12pt \"Lucida Bright\";")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_2.clicked.connect(self.detction)
        self.pushButton_3.clicked.connect(self.clear)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "  Face Expression:"))
        self.expression.setText(_translate("Dialog", ""))
        self.label_4.setText(_translate("Dialog", "Image Path"))
        self.pushButton.setText(_translate("Dialog", "Insert Path"))
        self.pushButton_2.setText(_translate("Dialog", "Detect"))
        self.pushButton_3.setText(_translate("Dialog", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Detection()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
