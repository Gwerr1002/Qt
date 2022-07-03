# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 15:35:02 2022

@author: Ortíz Montufar Gerardo
"""

from CalResistGUI import Ui_Form, QtWidgets

class MiApp(QtWidgets.QMainWindow):

    def __init__ (self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.multiplicadorDIC = {
            "Plata" : (0.01,"", "background-color: rgb(180, 180, 180)"),
            "Oro" : (0.1, "", "background-color: rgb(180, 130, 35)"),
            "Negro" : (1, "", "background-color: rgb(0, 0, 0)"),
            "Marron" :(10, "", "background-color: rgb(118, 51, 51)"),
            "Rojo" : (100, "", "background-color: rgb(255, 0, 0)"),
            "Naranja" : (1, " K", "background-color: rgb(255, 139, 3)"),
            "Amarillo" :(10, " K", "background-color: rgb(251, 244, 11)"),
            "Verde" : (100, " K", "background-color: rgb(0, 255, 0)"),
            "Azul" : (1, " M", "background-color: rgb(0, 0, 255)"),
            "Violeta" : (10, " M", "background-color: rgb(244, 11, 251)"),
            "Gris" : (100, " M", "background-color: rgb(119, 119, 119)")
        }

        self.colorDIC = {
            "Negro" : (0,"background-color: rgb(0, 0, 0)"),
            "Marron" : (1, "background-color: rgb(118, 51, 51)"),
            "Rojo" : (2, "background-color: rgb(255, 0, 0)"),
            "Naranja" : (3, "background-color: rgb(255, 139, 3)"),
            "Amarillo" : (4, "background-color: rgb(251, 244, 11)"),
            "Verde" : (5, "background-color: rgb(0, 255, 0)"),
            "Azul" : (6, "background-color: rgb(0, 0, 255)"),
            "Violeta" : (7, "background-color: rgb(244, 11, 251)"),
            "Gris" : (8, "background-color: rgb(119, 119, 119)"),
            "Blanco" : (9, "background-color: rgb(255, 255, 255)")
        }

        self.toleranciaDIC = {
            "Ninguna" : (.2, "background-color: rgb(212, 187, 111)"),
            "Plata" : (.1, "background-color: rgb(180, 180, 180)"),
            "Oro": (.05, "background-color: rgb(180, 130, 35)"),
            "Marron" : (.01, "background-color: rgb(118, 51, 51)"),
            "Rojo" : (.02, "background-color: rgb(255, 0, 0)"),
            "Verde" : (.005, "background-color: rgb(0, 255, 0)"),
            "Azul" : (.0025, "background-color: rgb(0, 0, 255)"),
            "Violeta": (.001,"background-color: rgb(244, 11, 251)"),
            "Gris" : (.0005, "background-color: rgb(119, 119, 119)")
            }

        self.valor1 = int(0)
        self.valor2 = int(0)
        self.valor3 = int(0)
        self.valor4 = int(0)
        self.Tol = int(0)
        self.notacion = str()

        self.ui.btn_resultado.clicked.connect(self.obtener_Resultado)

        self.ui.selec1.addItems (self.colorDIC.keys())
        self.ui.selec1.currentIndexChanged.connect (self.seleccion1)
        self.ui.selec1.setCurrentText("Negro")

        self.ui.selec2.addItems(self.colorDIC.keys())
        self.ui.selec2.currentIndexChanged.connect (self.seleccion2)
        self.ui.selec2.setCurrentText("Negro")

        self.ui.selec3.addItems(self.multiplicadorDIC.keys())
        self.ui.selec3.currentIndexChanged.connect (self.seleccion3)
        self.ui.selec3.setCurrentText("Negro")

        self.ui.selec4.addItems(self.toleranciaDIC.keys())
        self.ui.selec4.currentIndexChanged.connect (self.seleccion4)
        self.ui.selec4.setCurrentText("Ninguno")

    def seleccion1(self):
        self.valor1 = self.ui.selec1.currentText()
        self.valor1, color = self.colorDIC[self.valor1]
        self.ui.banda1.setStyleSheet(color)

    def seleccion2(self):
        self.valor2 = self.ui.selec2.currentText()
        self.valor2, color = self.colorDIC[self.valor2]
        self.ui.banda2.setStyleSheet(color)

    def seleccion3(self):
        self.valor3 = self.ui.selec3.currentText()
        self.valor3,self.notacion, color = self.multiplicadorDIC[self.valor3]
        self.ui.banda3.setStyleSheet(color)

    def seleccion4(self):
        self.valor4 = self.ui.selec4.currentText()
        self.valor4, color = self.toleranciaDIC[self.valor4]
        self.ui.banda4.setStyleSheet(color)
        self.Tol = "{}%".format(round(self.valor4*100,3))

    def obtener_Resultado(self):
        ValorR = float(str(self.valor1) + str(self.valor2))
        ValorR = ValorR*self.valor3

        Vmax = ValorR + ValorR*self.valor4
        Vmin = ValorR - ValorR*self.valor4

        self.ui.Resultado.setText(str(round(ValorR,3)) + self.notacion)
        self.ui.Tolerancia.setText(str(self.Tol))
        self.ui.maximo.setText(str(round(Vmax,3)) + self.notacion)
        self.ui.minimo.setText(str(round(Vmin,3)) + self.notacion)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())
