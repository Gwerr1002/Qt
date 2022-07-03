# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 23:24:00 2022

@author: gerard
"""
import sys
import numpy as np
from GUI import Ui_MainWindow
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigCanvas
import matplotlib.pyplot as plt

class Canvas(FigCanvas):
    
    def __init__(self, parent = None):
        self.fig, self.ax = plt.subplots(facecolor = 'gray')
        super().__init__(self.fig)
        self.ax.grid()
        self.ax.margins(x = 0)
        
        self.nivel1 = 10
        self.nivel2 = 1
        self.grafica_datos()
    
    def datos1(self, valor1):
        self.nivel1 = valor1*0.1
        
    def datos2(self, valor2):
        self.nivel2 = valor2*0.05
        
    def grafica_datos(self):
        plt.title("Grafica Sin")
        x = np.arange(-np.pi,10*np.pi,0.01)
        line, = self.ax.plot(x,self.nivel1*np.sin(self.nivel2*x),color = 'r',linewidth = 2)
        self.draw()
        line.set_ydata(np.sin(x) + 24)
        QtCore.QTimer.singleShot(10, self.grafica_datos)

class MiApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.grafica = Canvas(self)
        self.ui.verticalLayout_grafica.addWidget(self.grafica)
        self.ui.Slider1.valueChanged.connect(self.slider_uno)
        self.ui.Slider2.valueChanged.connect(self.slider_dos)
        
    def slider_uno(self, event):
        self.grafica.datos1(event)
        
    def slider_dos(self, event):
        self.grafica.datos2(event)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())