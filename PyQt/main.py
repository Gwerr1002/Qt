from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


if __name__ == '__main__':
    app = QApplication([]) #se debe iniciar primero la applicacion
    window = QMainWindow() #se establece una ventana prinipal
    window.show()          #Muestra la ventana principal
    app.exec_()            #Ejecuta la app
