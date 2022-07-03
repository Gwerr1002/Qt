from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainApp(QMainWindow):
    def __init__(self,parent = None, *args):
        super(MainApp, self).__init__(parent = parent)
        self.setMinimumSize(500,300)
        self.setWindowTitle("Text input")

        #texto input
        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("Usuario")
        self.user_input.setClearButtonEnabled(True) #aparece la x para borrar texto
        self.user_input.setGeometry(int(500/2-50), 50, 100, 30) #por default los objetos miden 100 px x 30 px
        #self.user_input.setMaxLength(2)#cantidad de caracteres permitidos
        self.user_input.setEchoMode(QLineEdit.PasswordEchoOnEdit) #desaparecen los caracteres y se remplazan por puntos
        '''Parametros que recibe setEchoMode
            QLineEdit.NoEcho -> No muestra los caracteres
            QLineEdit.Password -> Coloca puntos al escribir, no muestra los caracteres
        '''
        #self.user_input.setReadOnly(True) #bloquea la escritura y se cambia a solo lectura

        self.user_pass = QLineEdit(self)
        self.user_pass.setPlaceholderText("Contraseña")
        self.user_pass.setGeometry(int(500/2-50), 100, 100, 30)
        self.user_pass.setEchoMode(QLineEdit.Password)
        self.user_pass.setClearButtonEnabled(True)

        self.login_btn = QPushButton("Login",self)
        self.login_btn.setGeometry(int(500/2-50), 150, 100, 30)

        # ===================================
        #              Trigers

        self.user_input.returnPressed.connect(self.show_text) #evento cuando se presiona enter
        self.user_pass.returnPressed.connect(self.show_text)
        self.login_btn.clicked.connect(self.show_text)

        # ===================================

    def show_text(self):
        print(self.user_input.text()) #imprime en consola el texto ingresado
        print(self.user_pass.text())


if __name__ == '__main__':
    app = QApplication([])
    W = MainApp()
    W.show()
    sys.exit(app.exec_())
