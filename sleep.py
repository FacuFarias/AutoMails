# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sleep.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SleepBomb(object):
    def setupUi(self, SleepBomb):
        SleepBomb.setObjectName("SleepBomb")
        SleepBomb.resize(620, 362)
        SleepBomb.setStyleSheet("QMainWindow{\n"
"background-image: url(C:/Cursos/bomb-background.png);\n"
"background-attachment: scroll;\n"
"background-position: center right;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"font-size:30px;\n"
"color:white;\n"
"\n"
"\n"
"}\n"
"\n"
"QFrame#Menu\n"
"{\n"
"background-image: url(C:/Cursos/rec2.png);\n"
"background-size: 100% 100%;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background: qlineargradient(spread:pad, x1:1, y1:0.739, x2:1, y2:0.25, stop:0 #ee7624, stop:1 #f5a322);\n"
"border-radius:5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: #f56e22;\n"
"color:white;\n"
"font-size:20px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(spread:pad, x1:1, y1:0.739, x2:1, y2:0.5, stop:0 #ee7624, stop:1 #f5a322);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(SleepBomb)
        self.centralwidget.setObjectName("centralwidget")
        self.Menu = QtWidgets.QFrame(self.centralwidget)
        self.Menu.setGeometry(QtCore.QRect(310, 60, 261, 241))
        self.Menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Menu.setObjectName("Menu")
        self.pushButton = QtWidgets.QPushButton(self.Menu)
        self.pushButton.setGeometry(QtCore.QRect(60, 80, 141, 51))
        font = QtGui.QFont()
        font.setFamily("BankGothic Lt BT")
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Menu)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 160, 141, 51))
        font = QtGui.QFont()
        font.setFamily("BankGothic Lt BT")
        font.setPointSize(-1)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.Titulo_2 = QtWidgets.QLabel(self.Menu)
        self.Titulo_2.setGeometry(QtCore.QRect(90, 3, 161, 20))
        font = QtGui.QFont()
        font.setFamily("BankGothic Lt BT")
        font.setPointSize(-1)
        self.Titulo_2.setFont(font)
        self.Titulo_2.setObjectName("Titulo_2")
        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(30, 20, 371, 31))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(-1)
        self.Titulo.setFont(font)
        self.Titulo.setObjectName("Titulo")
        SleepBomb.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SleepBomb)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")
        SleepBomb.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SleepBomb)
        self.statusbar.setObjectName("statusbar")
        SleepBomb.setStatusBar(self.statusbar)

        self.retranslateUi(SleepBomb)
        QtCore.QMetaObject.connectSlotsByName(SleepBomb)

    def retranslateUi(self, SleepBomb):
        _translate = QtCore.QCoreApplication.translate
        SleepBomb.setWindowTitle(_translate("SleepBomb", "MainWindow"))
        self.pushButton.setText(_translate("SleepBomb", "Iniciar"))
        self.pushButton_2.setText(_translate("SleepBomb", "Cerrar"))
        self.Titulo_2.setText(_translate("SleepBomb", "Menu"))
        self.Titulo.setText(_translate("SleepBomb", "Sleep Bomb Crypto"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SleepBomb = QtWidgets.QMainWindow()
    ui = Ui_SleepBomb()
    ui.setupUi(SleepBomb)
    SleepBomb.show()
    sys.exit(app.exec_())