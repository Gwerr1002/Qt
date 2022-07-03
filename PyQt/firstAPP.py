from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainApp(QMainWindow):
    def __init__(self,parent = None, *args): #paren para transmitir info entre clases
        super(MainApp, self).__init__(parent = parent)
        '''Tamaño de una ventana:
            setMinimumSize()
            setMaximumSize()
            setFixedSize() -> Es tamaño fijo, no deja que se modifique el tamaño de la pantalla
        '''
        self.setMinimumSize(500,300) #impide que se pueda hacer más pequeña la pantalla
        #self.setMaximumSize(700,500) #impide que se agrande más de lo deseado
        "Título"
        self.setWindowTitle("Primera App")
        #label = QLabel("Hola :) este es un label", self) #con el self indicamos que debe ir en esta clase y no en un widget
        #self.widget = QWidget(self)

        width = self.frameGeometry().width()#retornar el largo y el alto de la clase padre
        height = self.frameGeometry().height()

        label = QLabel("Primer label", self) #si va en un widget iria en vez de self widget
        #print("El largo del elemento es ", label.frameGeometry().width(), "\nY el alto es: ", label.frameGeometry().height())#va a mostrar el tamaño del label
        #label.setGeometry(0,0,width,height) #recibe 4 parametros: posicion de izquierda a derecha - posicion de arriba a abajo - largo - alto
        label.setStyleSheet("background:#424242; color: #fff")
        label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter) #texto al centro y al fondo
        '''Qt.AlignCenter -> alinea al centro
            Qt.AlignLeft -> alinear a la izquierda
            Qt.AlignRight -> alinear a la derecha
            Qt.AlignBottom -> alinear al fondo
            Qt.AlignVCenter -> alinear verticalmente al centro (pordefecto)
        '''

        self.setCentralWidget(label) #expandir el label al tamño de la vetana



if __name__ == '__main__':
    app = QApplication(sys.argv) #se debe iniciar primero la applicacion
    window = MainApp() #se establece una ventana prinipal
    window.show()          #Muestra la ventana principal
    #app.exec_()            #Ejecuta la app
    sys.exit(app.exec_())
