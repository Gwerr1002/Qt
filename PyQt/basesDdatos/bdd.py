import re
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
#hashlib para cifrar
import hashlib

class MainApp(QMainWindow):
    def __init__(self,parent = None, *args):
        super(MainApp, self).__init__(parent = parent)
        self.conn = sql.connect('Data.db')
        self.c = self.conn.cursor()

        self.setMinimumSize(500,300)
        self.setWindowTitle("Mi App")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.label = QLabel(self.central_widget)

        #entrada de texto
        self.email = QLineEdit(self.central_widget)
        self.email.setPlaceholderText("Escribe tu e-mail")
        self.email.setClearButtonEnabled(True)

        '''
        Notas para SQLite
            - En DB browser crear nueva bdd
            - La tabla se llama usuarios
            - Añadir campos:
                + Un id de tipo entero - No vacío, una llave primaria (PK), y Autoincrementable (AI)
                + Campo email de tipo texto No vaío (MN)
        '''
        self.password = QLineEdit(self.central_widget)
        self.password.setPlaceholderText("Escribe tu contraseña")
        self.password.setClearButtonEnabled(True)
        self.password.setEchoMode(QLineEdit.Password)
        self.login = QPushButton("Login",self.central_widget)

        #Ver dimensiones de elemento
        #print(self.email.frameGeometry().height(),self.email.frameGeometry().width())
        self.login.clicked.connect(self.sign_in)
        self.email.returnPressed.connect(self.sign_in)
        self.password.returnPressed.connect(self.sign_in)

        #Mover elementos, ajuste de coordendas
        self.password.move(0, 40)
        self.login.move(0, 70)
        self.label.move(0,100)
        self.label.resize(self.frameGeometry().width(),self.label.frameGeometry().height())

    # =====================================
    #                 Slots
    def sign_in(self):
        email = self.email.text()
        password = hashlib.sha512(self.password.text().encode())
        #print(password.hexdigest())

        if email != "" and re.match('[^@]+@[^@]+\.[^@]+',email) and password != "":
            self.c.execute('INSERT INTO usuarios (email, password) VALUES ("{}","{}")'.format(email,password.hexdigest()))
            self.conn.commit()
            self.label.setText("Usuario registrado")
            self.label.setStyleSheet("background-color: green")
        else:
            self.label.setText("Email no válido")
            self.label.setStyleSheet("background-color: tomato; color: white")
    # =====================================


if __name__ == '__main__':
    app = QApplication([])
    W = MainApp()
    W.show()
    sys.exit(app.exec_())
