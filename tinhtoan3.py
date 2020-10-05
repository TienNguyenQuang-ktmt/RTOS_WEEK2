# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tinhtoan3.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

#tempValue = 0
#firstValue =0
#secondValue=0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(267, 488)
        MainWindow.setStyleSheet("")
        self.firstValue=0
        self.secondValue=0
        self.stt =True
        self.phepTinh=0
        #1:cong
        #2:Tru
        #3:nhan
        #4:chia
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnAC = QtWidgets.QPushButton(self.centralwidget)
        self.btnAC.setGeometry(QtCore.QRect(20, 170, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnAC.setFont(font)
        self.btnAC.setObjectName("btnAC")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(20, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(20, 290, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(20, 350, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(20, 410, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.btnAC_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btnAC_6.setGeometry(QtCore.QRect(80, 170, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnAC_6.setFont(font)
        self.btnAC_6.setObjectName("btnAC_6")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(80, 290, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(80, 350, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(80, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.btnPtram = QtWidgets.QPushButton(self.centralwidget)
        self.btnPtram.setGeometry(QtCore.QRect(140, 170, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnPtram.setFont(font)
        self.btnPtram.setObjectName("btnPtram")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(140, 290, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(140, 350, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(140, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.btnChia = QtWidgets.QPushButton(self.centralwidget)
        self.btnChia.setGeometry(QtCore.QRect(200, 170, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnChia.setFont(font)
        self.btnChia.setObjectName("btnChia")
        self.btnTru = QtWidgets.QPushButton(self.centralwidget)
        self.btnTru.setGeometry(QtCore.QRect(200, 290, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnTru.setFont(font)
        self.btnTru.setObjectName("btnTru")
        self.btnCong = QtWidgets.QPushButton(self.centralwidget)
        self.btnCong.setGeometry(QtCore.QRect(200, 350, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnCong.setFont(font)
        self.btnCong.setObjectName("btnCong")
        self.btnNhan = QtWidgets.QPushButton(self.centralwidget)
        self.btnNhan.setGeometry(QtCore.QRect(200, 230, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnNhan.setFont(font)
        self.btnNhan.setObjectName("btnNhan")
        self.btnBang = QtWidgets.QPushButton(self.centralwidget)
        self.btnBang.setGeometry(QtCore.QRect(200, 410, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnBang.setFont(font)
        self.btnBang.setObjectName("btnBang")
        self.btnPhay = QtWidgets.QPushButton(self.centralwidget)
        self.btnPhay.setGeometry(QtCore.QRect(140, 410, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnPhay.setFont(font)
        self.btnPhay.setObjectName("btnPhay")
        self.tvScreen = QtWidgets.QLabel(self.centralwidget)
        self.tvScreen.setGeometry(QtCore.QRect(20, 20, 231, 121))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tvScreen.setFont(font)
        self.tvScreen.setStyleSheet("boder-radius:20px;\n"
"backdround-color:rgb(40, 38, 49);")
        self.tvScreen.setObjectName("tvScreen")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #ham nhan phim
        self.btn0.clicked.connect(self.phimKhong)
        self.btn1.clicked.connect(self.phimMot)
        self.btn2.clicked.connect(self.phimHai)
        self.btn3.clicked.connect(self.phimBa)
        self.btn4.clicked.connect(self.phimBon)
        self.btn5.clicked.connect(self.phimNam)
        self.btn6.clicked.connect(self.phimSau)
        self.btn7.clicked.connect(self.phimBay)
        self.btn8.clicked.connect(self.phimTam)
        self.btn9.clicked.connect(self.phimChin)
        self.btnAC.clicked.connect(self.phimXoa)
        self.btnBang.clicked.connect(self.phimBang)
        self.btnChia.clicked.connect(self.phimChia)
        self.btnNhan.clicked.connect(self.phimNhan)
        self.btnCong.clicked.connect(self.phimCong)
        self.btnTru.clicked.connect(self.phimTru)
        self.btnPtram.clicked.connect(self.phimPhanTram)

    def phimKhong(self):
        if(self.stt):
            self.firstValue= self.firstValue*10+0
            self.tvScreen.setText(str(self.firstValue))
        else:
            self.secondValue= self.secondValue*10+0
            self.tvScreen.setText(self.tvScreen.text()+ "0")
    def phimMot(self):
        if(self.stt):
            self.firstValue= self.firstValue*10+1
            self.tvScreen.setText(str(self.firstValue))
        else:
            self.secondValue= self.secondValue*10+1
            self.tvScreen.setText(self.tvScreen.text()+ "1")
    def phimHai(self):
        if(self.stt):
            self.firstValue= self.firstValue*10+2
            self.tvScreen.setText(str(self.firstValue))
        else:
            self.secondValue= self.secondValue*10+2
            self.tvScreen.setText(self.tvScreen.text()+ "2")
    def phimBa(self):
        if(self.stt):
            self.firstValue= self.firstValue*10+3
            self.tvScreen.setText(str(self.firstValue))
        else:
            self.secondValue= self.secondValue*10+3
            self.tvScreen.setText(self.tvScreen.text()+ "3")
    def phimBon(self):
        if(self.stt):
            self.firstValue= self.firstValue*10+4
            self.tvScreen.setText(str(self.firstValue))
        else:
            self.secondValue= self.secondValue*10+4
            self.tvScreen.setText(self.tvScreen.text()+ "4")
    def phimNam(self):
        if(self.stt):
            self.firstValue= self.firstValue*10+5
            self.tvScreen.setText(str(self.firstValue))
        else:
            self.secondValue= self.secondValue*10+5
            self.tvScreen.setText(self.tvScreen.text()+ "5")
    def phimSau(self):
        if(self.stt):
            self.firstValue= self.firstValue*10+6
            self.tvScreen.setText(str(self.firstValue))
        else:
            self.secondValue= self.secondValue*10+6
            self.tvScreen.setText(self.tvScreen.text()+ "6")
    def phimBay(self):
        if(self.stt):
            self.firstValue= self.firstValue*10+7
            self.tvScreen.setText(str(self.firstValue))
        else:
            self.secondValue= self.secondValue*10+7
            self.tvScreen.setText(self.tvScreen.text()+ "7")
    def phimTam(self):
        if(self.stt):
            self.firstValue= self.firstValue*10+8
            self.tvScreen.setText(str(self.firstValue))
        else:
            self.secondValue= self.secondValue*10+8
            self.tvScreen.setText(self.tvScreen.text()+ "8")
    def phimChin(self):
        if(self.stt):
            self.firstValue= self.firstValue*10+9
            self.tvScreen.setText(str(self.firstValue))
        else:
            self.secondValue= self.secondValue*10+9
            self.tvScreen.setText(self.tvScreen.text()+ "9")
    def phimXoa(self):
        self.firstValue=0
        self.secondValue=0
        self.stt=True
        self.tvScreen.setText(" ")
    def phimChia(self):
        self.phepTinh=4
        self.stt = False
        self.tvScreen.setText(str(self.firstValue)+"/")
    def phimNhan(self):
        self.phepTinh=3
        self.stt = False
        self.tvScreen.setText(str(self.firstValue)+"x")
    def phimCong(self):
        self.phepTinh=1
        self.stt = False
        self.tvScreen.setText(str(self.firstValue)+"+")
    def phimTru(self):
        self.phepTinh=2
        self.stt = False
        self.tvScreen.setText(str(self.firstValue)+"-")
    def phimBang(self):
        if self.phepTinh==1:
            kq=self.firstValue+self.secondValue
        elif self.phepTinh==2:
            kq=self.firstValue-self.secondValue
        elif self.phepTinh==3:
            kq=self.firstValue*self.secondValue
        elif self.phepTinh==4:
            kq=self.firstValue/self.secondValue
        self.tvScreen.setText(str(kq))
        self.firstValue=0
        self.secondValue=0
        self.stt=True

    def phimPhanTram(self):
        self.tvScreen.setText(str(self.firstValue)+"%")
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAC.setText(_translate("MainWindow", "AC"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btnAC_6.setText(_translate("MainWindow", "hi"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btnPtram.setText(_translate("MainWindow", "%"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btnChia.setText(_translate("MainWindow", "/"))
        self.btnTru.setText(_translate("MainWindow", "-"))
        self.btnCong.setText(_translate("MainWindow", "+"))
        self.btnNhan.setText(_translate("MainWindow", "x"))
        self.btnBang.setText(_translate("MainWindow", "="))
        self.btnPhay.setText(_translate("MainWindow", ","))
        self.tvScreen.setText(_translate("MainWindow", "0000"))

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
