# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Face Recognition\Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4



from PyQt5 import QtCore, QtGui, QtWidgets
from FERRecognition import Ui_Recognition


class Ui_Main(object):
    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()

    def login(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Recognition()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 650)
        #Dialog.setStyleSheet("QDialog{background-image: url(../FER_CNN/Images/mainBG.JPG);}")
        self.label = QtWidgets.QLabel(Dialog)
        # setting  the geometry of window
        # setGeometry(left, top, width, height)
        self.label.setGeometry(QtCore.QRect(200, 10, 581, 121))
        self.label.setStyleSheet("font: 50pt \"\";\n""font: 100 25pt \"Lucida Bright\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.clicked.connect(self.login)
        self.pushButton.setGeometry(QtCore.QRect(250, 380, 161, 41))
        self.pushButton.setStyleSheet("font: 12pt \"\";\n""font: 100 12pt \"Lucida Bright\";")
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Facial Expression Recognition"))
        self.label.setText(_translate("Dialog", "Face Expression Recognition"))
        self.pushButton.setText(_translate("Dialog", "Click Here"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
