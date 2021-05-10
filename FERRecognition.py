from PyQt5 import QtCore, QtGui, QtWidgets
from Detection import Ui_Detection
from FER_Camera import detection_FER


class Ui_Recognition(object):
    def FER_Image(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Detection()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
    def FER_Camera(self):
        detection_FER()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 650)
        #Dialog.setStyleSheet("QDialog{background-image: url(../FER_CNN/Images/user.jpg);}")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 150, 251, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("font: 12pt \"\";\n""font: 63 12pt \"Lucida Bright\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 250, 251, 61))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("font: 12pt \"\";\n""font: 63 12pt \"Lucida Bright\";")
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 10, 91, 91))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(225, 252, 58, 54))

        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 152, 58, 54))

        self.label_3.setText("")
        self.label_3.setObjectName("label_3")


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.FER_Image)
        self.pushButton_2.clicked.connect(self.FER_Camera)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select An Option"))
        self.pushButton.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Image"))
        self.pushButton_2.setText(_translate("Dialog", "Camera"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Recognition()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
