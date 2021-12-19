import sys
import time
from main import *
from nuevoalumno import *
from enviarmails import *
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread
import requests
from PIL import Image, ImageDraw, ImageFont
import sqlite3
import numpy as np
import time
import smtplib
from email.message import EmailMessage
from email.mime.image import MIMEImage
class DialogNotas(QWidget):
    def __init__(self):
        super().__init__()
        
        self.notas = QtWidgets.QDialog()
        self.uinotas = Ui_Notas()
        self.uinotas.setupUi(self.notas)
        self.notas.show()

        self.uinotas.pushButton.clicked.connect(self.enviar)
        self.uinotas.pushButton_2.clicked.connect(self.notas.close)

    def enviar(self):

        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()

        # Usuario y contraseña
        usuario = 'facufarias93@gmail.com'
        password = 'locoreloco3'

        server.login(usuario, password)
        self.conexion=sqlite3.connect("alumnos.db")


        query="select nombre,mail,p1,p2,p3,tp from curso3"
        self.cursor=self.conexion.execute(query)
        #rows=self.cursor.rowcount()
        
        for fila in self.cursor:

            cuerpo = "Hola "+fila[0]+ " ¿Como estas? \n"

            if self.uinotas.cb_1.isChecked():
                cuerpo= cuerpo +  "La nota del parcial 1 es de:  "+str(fila[2])+"\n"
                
            if self.uinotas.cb_2.isChecked():
                cuerpo= cuerpo + "La nota del parcial 2 es de:  "+ str(fila[3])+"\n"
                
            if self.uinotas.cb_3.isChecked():
                cuerpo= cuerpo + "La nota del parcial 3 es de:  "+ str(fila[4])+"\n"
                
            if self.uinotas.cb_tp.isChecked():
                cuerpo= cuerpo + "La nota del tp es de:  "+ str(fila[5])+"\n"
                
            msg=EmailMessage()
            msg['From']="facufarias93@gmail.com"
            msg['To']=str(fila[1])
            msg['Subject']='Notas Parcial'
            
            print(cuerpo)
            msg.set_content(cuerpo)
            server.send_message(msg)
            #time.sleep(2)
        
        server.quit()

class DialogNotif(QWidget):
    def __init__(self):
        super().__init__()
        
        self.notificaciones = QtWidgets.QDialog()
        self.uinotif = Ui_NewAlumn()
        self.uinotif.setupUi(self.notificaciones)
        self.notificaciones.show()

        self.uinotif.b_agregar.clicked.connect(self.agrego)
    
    def agrego(self):
        nombre=self.uinotif.le_nombre.text()
        mail=self.uinotif.le_mail.text()
        self.conexion=sqlite3.connect("alumnos.db")
        query= 'insert into curso3(nombre,mail) values (?,?)'
        self.conexion.execute(query,(nombre,mail,))
        self.conexion.commit()
        self.conexion.close()
        
            
        mi_app.actualizartabla()
        
        self.notificaciones.close()


class Ventana(QWidget):

    def __init__(self,parent=None):

        QtWidgets.QWidget.__init__(self,parent)
        self.ui=Ui_MainWindow()
        self.mw= QtWidgets.QMainWindow()
        self.ui.setupUi(self.mw)
        self.mw.show()

        self.actualizartabla()
        
        self.ui.b_agregar.clicked.connect(self.agregar)
        self.ui.b_certif.clicked.connect(self.certificado)
        self.ui.b_mails.clicked.connect(self.mails)
        self.ui.b_eliminar.clicked.connect(self.eliminar)
        self.ui.T_main.itemChanged.connect(self.cambiarValor)
        self.ui.T_main.cellClicked[int,int].connect(self.ui.l_cell.setNum)


    def eliminar(self):
        self.conexion=sqlite3.connect("alumnos.db")
        row=int(mi_app.ui.l_cell.text())
        nombre=mi_app.ui.T_main.item(row,0).text()
        query="delete from curso3 where nombre=(?)"
        self.conexion.execute(query,(nombre,))
        self.conexion.commit()

        mi_app.actualizartabla()

    def agregar(self):
        self.dianotif=DialogNotif()
        

    def actualizartabla(self):
        self.ui.T_main.blockSignals(True)
        rows=self.ui.T_main.rowCount()
        if rows!=0:
            i=0
            while i<=rows:
                mi_app.ui.T_main.removeRow(rows-1-i)
                i=i+1
        self.conexion=sqlite3.connect("alumnos.db")
        
        self.cursor = self.conexion.execute("select nombre,mail,p1,p2,p3,tp,cert from curso3")
        
        self.i=0
        for fila in self.cursor:
            self.ui.T_main.insertRow(self.i)
            item=QtWidgets.QTableWidgetItem(fila[0])
            self.ui.T_main.setItem(self.i,0,item)
            item=QtWidgets.QTableWidgetItem(fila[1])
            self.ui.T_main.setItem(self.i,1,item)
            item=QtWidgets.QTableWidgetItem(str(fila[2]))
            self.ui.T_main.setItem(self.i,2,item)
            item=QtWidgets.QTableWidgetItem(str(fila[3]))
            self.ui.T_main.setItem(self.i,3,item)
            item=QtWidgets.QTableWidgetItem(str(fila[4]))
            self.ui.T_main.setItem(self.i,4,item)
            item=QtWidgets.QTableWidgetItem(str(fila[5]))
            self.ui.T_main.setItem(self.i,5,item)
            item=QtWidgets.QTableWidgetItem(str(fila[6]))
            self.ui.T_main.setItem(self.i,6,item)
            try:
                promedio= (float(fila[2])+float(fila[3])+float(fila[4]))/3
            except:
                promedio=0
            if fila[2] is None or fila[3] is None or fila[4] is None or promedio<7:
                item=QtWidgets.QTableWidgetItem(str("Falta Alcanzar"))
                self.ui.T_main.setItem(self.i,6,item)
                query="update curso3 set cert='FA' where nombre=(?)"
                self.conexion.execute(query,(fila[0],))
                self.conexion.commit()


            else:
                item=QtWidgets.QTableWidgetItem(str("Alcanzado"))
                self.ui.T_main.setItem(self.i,6,item)
                query="update curso3 set cert='A' where nombre=(?)"
                self.conexion.execute(query,(fila[0],))
                self.conexion.commit()



            self.i=self.i+1

            


        
        self.ui.l_alumnos.setText("Alumnos:  "+str(self.i))
        self.conexion.close()
        self.ui.T_main.blockSignals(False)


    def certificado(self):

        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()

        # Usuario y contraseña
        usuario = 'facufarias93@gmail.com'
        password = 'locoreloco3'

        server.login(usuario, password)


        curso='Automatización y web scrapping'
        
        color="black"
        font = ImageFont.truetype("arial.ttf", 50)
        firma1=Image.open("Planilla enviamails/firma1.png")
        firma2=Image.open("Planilla enviamails/firma 2.png")
        f=firma1.resize((200,100))
        size_curso = font.getsize(curso)
        self.conexion=sqlite3.connect("alumnos.db")
        
        self.cursor = self.conexion.execute("select * from curso3")
        for fila in self.cursor:
            if fila[7]=='A':
                certifi=Image.open('Planilla enviamails/certificado.png')
                draw = ImageDraw.Draw(certifi)
                promedio = (float(fila[3])+float(fila[4])+float(fila[5]))/3
                nombre=fila[1]
                size_text = font.getsize(nombre)
                
                draw.text(((certifi.size[0]-size_text[0])/2,(certifi.size[1]-size_text[1])/2),nombre,font=font,fill=color)
                draw.text(((certifi.size[0]-size_curso[0])/2,(certifi.size[1]/2)+155),curso,font=font,fill=color)
                draw.text(((certifi.size[0]-size_curso[0])/2,(certifi.size[1]/2)+220),'Con un promedio de:'+str(promedio),font=font,fill=color)
                #certifi.paste(f,(int(certifi.size[0]/4),int(certifi.size[1]/4*3)),f)
                #certifi.paste(f,(int(certifi.size[0]*0.6),int(certifi.size[1]/4*3)),f)
                certifi.save(nombre+'.png')


                msg=EmailMessage()
                msg['From']="facufarias93@gmail.com"
                msg['To']=str(fila[2])
                msg['Subject']='Notas Parcial'
                cuerpo = "Hola "+nombre + "\n"


                path_imagen = nombre+'.png' 

                with open(path_imagen, 'rb') as f:
                    image_data = f.read()
                    image_name = f.name
                    print(image_name)


                #image = MIMEImage(image_data, name=os.path.basename(image_name))
                #msg.attach(image)
                
                msg.set_content(cuerpo)
                msg.add_attachment(image_data, maintype='image', subtype='png', filename=image_name)
                server.send_message(msg)
        
        self.conexion.close()
        server.quit()


    def mails(self):
        self.diamails=DialogNotas()
        pass
    def cambiarValor(self,item):
        row = item.row()
        col = item.column()
        if col == 1:
            query="update curso3 set mail=(?) where nombre=(?)"
        elif col==2:
            query="update curso3 set p1=(?) where nombre=(?)"
        elif col==3:
            query="update curso3 set p2=(?) where nombre=(?)"
        elif col==4:
            query="update curso3 set p3=(?) where nombre=(?)"
        elif col==5:
            query="update curso3 set tp=(?) where nombre=(?)"
        elif col==6:
            query="update curso3 set cert=(?) where nombre=(?)"
        data=mi_app.ui.T_main.item(row,col).text()
        nombre=mi_app.ui.T_main.item(row,0).text()
        self.conexion=sqlite3.connect("alumnos.db")
        self.conexion.execute(query,(data,nombre,))
        self.conexion.commit()
        
        self.conexion.close()
        self.actualizartabla()
        

        
        

if __name__ == "__main__":
    mi_aplicacion=QApplication(sys.argv)
    mi_app = Ventana()
    sys.exit(mi_aplicacion.exec_())
    