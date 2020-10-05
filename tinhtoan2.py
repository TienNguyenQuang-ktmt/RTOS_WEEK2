# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tinhtoan2.ui'
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
        self.label.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.edtA = QtWidgets.QLineEdit(Dialog)
        self.edtA.setGeometry(QtCore.QRect(50, 20, 113, 20))
        self.edtA.setObjectName("edtA")
        self.edtB = QtWidgets.QLineEdit(Dialog)
        self.edtB.setGeometry(QtCore.QRect(50, 50, 113, 20))
        self.edtB.setObjectName("edtB")
        self.tvKetQua = QtWidgets.QLabel(Dialog)
        self.tvKetQua.setGeometry(QtCore.QRect(50, 230, 330, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.tvKetQua.setFont(font)
        self.tvKetQua.setText("")
        self.tvKetQua.setObjectName("tvKetQua")
        self.edtD = QtWidgets.QLineEdit(Dialog)
        self.edtD.setGeometry(QtCore.QRect(220, 50, 113, 20))
        self.edtD.setObjectName("edtD")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(190, 50, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(190, 20, 47, 13))
        self.label_4.setObjectName("label_4")
        self.edtC = QtWidgets.QLineEdit(Dialog)
        self.edtC.setGeometry(QtCore.QRect(220, 20, 113, 20))
        self.edtC.setObjectName("edtC")
        self.cbBox = QtWidgets.QComboBox(Dialog)
        self.cbBox.setGeometry(QtCore.QRect(110, 120, 151, 22))
        self.cbBox.setCurrentText("")
        self.cbBox.setObjectName("cbBox")
        #add
        self.cbBox.addItem("Tinh Tong")
        self.cbBox.addItem("Tinh Tich") 
        self.cbBox.addItem("Tinh Max")
        self.cbBox.addItem("Sap Tang")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #ham nhan nut
        self.btnKetQua.clicked.connect(self.showKetQua)
    def showKetQua(self):
        if self.cbBox.currentText()=="Tinh Tong":
            kq=float(self.edtA.text())+float(self.edtB.text())+float(self.edtC.text())+float(self.edtD.text())
            self.tvKetQua.setText("Ket qua= "+str(kq))
        elif self.cbBox.currentText()=="Tinh Tich":
            self.tvKetQua.setText("Ket qua= "+str(float(self.edtA.text())*float(self.edtB.text())*float(self.edtC.text())*float(self.edtD.text())))  
        elif self.cbBox.currentText()=="Tinh Max":
            max= float(self.edtA.text())
            arr =[float(self.edtA.text()),float(self.edtB.text()),float(self.edtC.text()),float(self.edtD.text())]
            for i in arr:
                if i> max:
                    max=i
            self.tvKetQua.setText("Max = "+str(max))
        else :
            arr =[float(self.edtA.text()),float(self.edtB.text()),float(self.edtC.text()),float(self.edtD.text())]
            for i in range(0,len(arr)-1):
                for x in range(i+1,len(arr)):
                    if arr[i]> arr[x]:
                        temp = arr[i]
                        arr[i]=arr[x]
                        arr[x]=temp
            #stringKQ= str(float(arr[0]))+str(float(arr[1]))+str(float(arr[2]))+str(float(arr[3]))
            self.tvKetQua.setText("Tang Dan: "+str(int(arr[0]))+":"+str(int(arr[1]))+":"+str(int(arr[2]))+":"+str(int(arr[3])))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btnKetQua.setText(_translate("Dialog", "Tính Toán"))
        self.label.setText(_translate("Dialog", "số A"))
        self.label_2.setText(_translate("Dialog", "số B"))
        self.label_3.setText(_translate("Dialog", "số D"))
        self.label_4.setText(_translate("Dialog", "số C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
