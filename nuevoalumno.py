# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevoalumno.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewAlumn(object):
    def setupUi(self, NewAlumn):
        NewAlumn.setObjectName("NewAlumn")
        NewAlumn.resize(400, 151)
        NewAlumn.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"}\n"
"\n"
"QDialog{\n"
"background: rgba(2, 14, 38, 255)\n"
"\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"background: #020E26;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QToolButton\n"
"{\n"
"background: #2d89ef;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QToolButton:hover\n"
"{\n"
"background:  #2b5797;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"background:rgba(2, 14, 38, 255);\n"
"border:none;\n"
"border-bottom: 1px solid white;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"background: #2d89ef;\n"
"color: white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #2b5797;\n"
"color: white;\n"
"border-radius: 5px;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QGroupBox{\n"
"color:white;\n"
"\n"
"}\n"
"\n"
"QGroupBox#ref{\n"
"color:white;\n"
"}\n"
"\n"
"QLabel#Titulo\n"
"{\n"
"font-size:20px;\n"
"}\n"
"QTableWidget\n"
"{\n"
"color:white;\n"
"text-align:center;\n"
"}")
        self.frame = QtWidgets.QFrame(NewAlumn)
        self.frame.setGeometry(QtCore.QRect(20, 55, 371, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.le_mail = QtWidgets.QLineEdit(self.frame)
        self.le_mail.setGeometry(QtCore.QRect(80, 30, 261, 20))
        self.le_mail.setObjectName("le_mail")
        self.l_mail = QtWidgets.QLabel(self.frame)
        self.l_mail.setGeometry(QtCore.QRect(11, 32, 47, 13))
        self.l_mail.setObjectName("l_mail")
        self.l_nombre = QtWidgets.QLabel(self.frame)
        self.l_nombre.setGeometry(QtCore.QRect(10, 14, 47, 13))
        self.l_nombre.setObjectName("l_nombre")
        self.le_nombre = QtWidgets.QLineEdit(self.frame)
        self.le_nombre.setGeometry(QtCore.QRect(80, 10, 261, 20))
        self.le_nombre.setObjectName("le_nombre")
        self.Titulo = QtWidgets.QLabel(NewAlumn)
        self.Titulo.setGeometry(QtCore.QRect(29, 24, 351, 31))
        self.Titulo.setObjectName("Titulo")
        self.b_agregar = QtWidgets.QPushButton(NewAlumn)
        self.b_agregar.setGeometry(QtCore.QRect(200, 120, 75, 23))
        self.b_agregar.setObjectName("b_agregar")
        self.b_cancelar = QtWidgets.QPushButton(NewAlumn)
        self.b_cancelar.setGeometry(QtCore.QRect(280, 120, 75, 23))
        self.b_cancelar.setObjectName("b_cancelar")

        self.retranslateUi(NewAlumn)
        QtCore.QMetaObject.connectSlotsByName(NewAlumn)

    def retranslateUi(self, NewAlumn):
        _translate = QtCore.QCoreApplication.translate
        NewAlumn.setWindowTitle(_translate("NewAlumn", "Dialog"))
        self.l_mail.setText(_translate("NewAlumn", "Mail:"))
        self.l_nombre.setText(_translate("NewAlumn", "Nombre:"))
        self.Titulo.setText(_translate("NewAlumn", "Nuevo alumno"))
        self.b_agregar.setText(_translate("NewAlumn", "Agregar"))
        self.b_cancelar.setText(_translate("NewAlumn", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewAlumn = QtWidgets.QDialog()
    ui = Ui_NewAlumn()
    ui.setupUi(NewAlumn)
    NewAlumn.show()
    sys.exit(app.exec_())
