# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tinhtoan.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.btnKetQua = QtWidgets.QPushButton(Dialog)
        self.btnKetQua.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.btnKetQua.setObjectName("btnKetQua")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 20, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.edtA = QtWidgets.QLineEdit(Dialog)
        self.edtA.setGeometry(QtCore.QRect(160, 20, 113, 20))
        self.edtA.setObjectName("edtA")
        self.edtB = QtWidgets.QLineEdit(Dialog)
        self.edtB.setGeometry(QtCore.QRect(160, 50, 113, 20))
        self.edtB.setObjectName("edtB")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 371, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.rBCong = QtWidgets.QRadioButton(self.groupBox)
        self.rBCong.setChecked(True)    #default stateChecked
        self.rBCong.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.rBCong.setObjectName("rBCong")
        self.rBTru = QtWidgets.QRadioButton(self.groupBox)
        self.rBTru.setGeometry(QtCore.QRect(110, 30, 82, 17))
        self.rBTru.setObjectName("rBTru")
        self.rBNhan = QtWidgets.QRadioButton(self.groupBox)
        self.rBNhan.setGeometry(QtCore.QRect(200, 30, 82, 17))
        self.rBNhan.setObjectName("rBNhan")
        self.rBChia = QtWidgets.QRadioButton(self.groupBox)
        self.rBChia.setGeometry(QtCore.QRect(290, 30, 82, 17))
        self.rBChia.setObjectName("rBChia")
        self.tvKetQua = QtWidgets.QLabel(Dialog)
        self.tvKetQua.setGeometry(QtCore.QRect(50, 230, 301, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.tvKetQua.setFont(font)
        self.tvKetQua.setText("")
        self.tvKetQua.setObjectName("tvKetQua")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btnKetQua.clicked.connect(self.showketQua)
    def showketQua(self):
        a =float(self.edtA.text())
        b =float(self.edtB.text())
        if self.rBCong.isChecked():
            kq =a+b
        if self.rBTru.isChecked():
            kq =a-b    
        if self.rBNhan.isChecked():
            kq =a*b
        if self.rBChia.isChecked():
            kq =a/b
        self.tvKetQua.setText("Kết Quả = " +str(kq))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnKetQua.setText(_translate("Dialog", "Tính Toán"))
        self.label.setText(_translate("Dialog", "số A"))
        self.label_2.setText(_translate("Dialog", "số B"))
        self.rBCong.setText(_translate("Dialog", "Cộng"))
        self.rBTru.setText(_translate("Dialog", "Trừ"))
        self.rBNhan.setText(_translate("Dialog", "Nhân"))
        self.rBChia.setText(_translate("Dialog", "Chia"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
