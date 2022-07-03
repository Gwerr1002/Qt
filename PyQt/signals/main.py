from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainApp(QMainWindow):
    def __init__(self,parent = None, *args):
        super(MainApp, self).__init__(parent = parent)
        self.setMinimumSize(500,300)
        self.setWindowTitle("Primera App")

        msg = "Este dato ha sido enviado por una señal y recibido por un slot"

        #Botones
        self.btn_lambda = QPushButton("send data", self)
        self.single_btn = QPushButton("show info", self)
        #Posicion de los Botones
        self.btn_lambda.setGeometry(0,0,70,40)
        self.single_btn.setGeometry(80,0,70,40)

        #señales
        self.btn_lambda.clicked.connect(lambda: self.slot_with_params("Parametro enviado")) #conectarse a un slot
        self.single_btn.clicked.connect(self.single_slot) #notar que con lambda se envían parametros

        #label
        self.label = QLabel("Haz click en mi",self)
        self.label.setGeometry(0, 120,150, 150)
        self.label.mousePressEvent = self.single_slot #al construit el metodo debe recibir un Parametro

        # ================================
        #             Slots
    def slot_with_params(self,msg):
        print(msg)

    def single_slot(self, event):
        print(event)
        print("Se ha hecho click")
        #           End Slots
        #=================================


if __name__ == '__main__':
    app = QApplication(sys.argv) #se debe iniciar primero la applicacion
    window = MainApp() #se establece una ventana prinipal
    window.show()          #Muestra la ventana principal
    #app.exec_()            #Ejecuta la app
    sys.exit(app.exec_())
