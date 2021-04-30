# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\QT\Face Recognition\Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4



from PyQt5 import QtCore, QtGui, QtWidgets
from Admin import Ui_Admin
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
        uid = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        log = self.comboBox.currentText()
        if uid=="null" or uid=="" or pwd=="null" or pwd=="":
            self.alertmsg("error","Please Enter UserId and Password")
        elif log=="Admin" and uid=="admin" and pwd=="admin":
            self.Dialog = QtWidgets.QDialog()
            self.ui = Ui_Admin()
            self.ui.setupUi(self.Dialog)
            self.Dialog.show()
        elif log=="User" and uid=="user" and pwd=="user":
            self.Dialog = QtWidgets.QDialog()
            self.ui = Ui_Recognition()
            self.ui.setupUi(self.Dialog)
            self.Dialog.show()
        else:
            self.alertmsg("Failed","Please Enter Valid Crendentials")
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 650)
        Dialog.setStyleSheet("QDialog{background-image: url(../FER_CNN/Images/main.jpg);}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(420, 10, 581, 121))
        self.label.setStyleSheet("font: 28pt \"Copperplate Gothic Bold\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(108, 186, 241, 23));\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(480, 160, 331, 451))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(108, 186, 241, 23));")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(60, 163, 241, 41))
        self.lineEdit.setStyleSheet("font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 231, 241, 41))
        self.lineEdit_2.setStyleSheet("font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(60, 298, 241, 41))
        self.comboBox.setStyleSheet("font: 75 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.clicked.connect(self.login)
        self.pushButton.setGeometry(QtCore.QRect(100, 380, 161, 41))
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.752632 rgba(102, 47, 118, 232), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Bernard MT Condensed\";")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(132, 8, 81, 81))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(58, 194, 55, 0));\n"
"background-image: url(:/back/homeico.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(145, 75, 141, 51))
        self.label_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(58, 194, 55, 0));")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Face Expression\n"
"Recognition"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "UserId"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "PassWord"))
        self.comboBox.setItemText(0, _translate("Dialog", "User"))
        self.comboBox.setItemText(1, _translate("Dialog", "Admin"))
        self.pushButton.setText(_translate("Dialog", "LogIn"))
        self.label_3.setText(_translate("Dialog", "Home"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
