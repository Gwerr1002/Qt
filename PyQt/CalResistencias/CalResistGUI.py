# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalReistGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(390, 319)
        Form.setStyleSheet("background-color: rgb(76, 57, 115);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 47, 13))
        self.label.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(310, 40, 47, 13))
        self.label_2.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 12, 47, 81))
        self.label_3.setStyleSheet("background-color: rgb(212, 187, 111);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(270, 10, 47, 81))
        self.label_4.setStyleSheet("background-color: rgb(212, 187, 111);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 20, 161, 61))
        self.label_5.setStyleSheet("background-color: rgb(212, 187, 111);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.banda1 = QtWidgets.QLabel(Form)
        self.banda1.setGeometry(QtCore.QRect(80, 10, 16, 81))
        self.banda1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.banda1.setText("")
        self.banda1.setObjectName("banda1")
        self.banda2 = QtWidgets.QLabel(Form)
        self.banda2.setGeometry(QtCore.QRect(130, 20, 16, 61))
        self.banda2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.banda2.setText("")
        self.banda2.setObjectName("banda2")
        self.banda3 = QtWidgets.QLabel(Form)
        self.banda3.setGeometry(QtCore.QRect(170, 20, 16, 61))
        self.banda3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.banda3.setText("")
        self.banda3.setObjectName("banda3")
        self.banda4 = QtWidgets.QLabel(Form)
        self.banda4.setGeometry(QtCore.QRect(240, 20, 16, 61))
        self.banda4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.banda4.setText("")
        self.banda4.setObjectName("banda4")
        self.selec1 = QtWidgets.QComboBox(Form)
        self.selec1.setGeometry(QtCore.QRect(30, 140, 69, 22))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(15)
        self.selec1.setFont(font)
        self.selec1.setStyleSheet("background-color: rgb(255, 57, 60);\n"
"color: rgb(255, 255, 255);")
        self.selec1.setObjectName("selec1")
        self.selec2 = QtWidgets.QComboBox(Form)
        self.selec2.setGeometry(QtCore.QRect(120, 140, 69, 22))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(15)
        self.selec2.setFont(font)
        self.selec2.setStyleSheet("background-color: rgb(255, 57, 60);\n"
"color: rgb(255, 255, 255);")
        self.selec2.setObjectName("selec2")
        self.selec3 = QtWidgets.QComboBox(Form)
        self.selec3.setGeometry(QtCore.QRect(210, 140, 69, 22))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(15)
        self.selec3.setFont(font)
        self.selec3.setStyleSheet("background-color: rgb(255, 57, 60);\n"
"color: rgb(255, 255, 255);")
        self.selec3.setObjectName("selec3")
        self.selec4 = QtWidgets.QComboBox(Form)
        self.selec4.setGeometry(QtCore.QRect(290, 140, 69, 22))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(15)
        self.selec4.setFont(font)
        self.selec4.setStyleSheet("background-color: rgb(255, 57, 60);\n"
"color: rgb(255, 255, 255);")
        self.selec4.setObjectName("selec4")
        self.Tol_title = QtWidgets.QLabel(Form)
        self.Tol_title.setGeometry(QtCore.QRect(30, 200, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(20)
        self.Tol_title.setFont(font)
        self.Tol_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.Tol_title.setObjectName("Tol_title")
        self.Tolerancia = QtWidgets.QLabel(Form)
        self.Tolerancia.setGeometry(QtCore.QRect(120, 200, 47, 41))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(20)
        self.Tolerancia.setFont(font)
        self.Tolerancia.setStyleSheet("color: rgb(255, 255, 255);")
        self.Tolerancia.setText("")
        self.Tolerancia.setObjectName("Tolerancia")
        self.maximo = QtWidgets.QLabel(Form)
        self.maximo.setGeometry(QtCore.QRect(190, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(20)
        self.maximo.setFont(font)
        self.maximo.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(71, 94, 223);")
        self.maximo.setText("")
        self.maximo.setObjectName("maximo")
        self.minimo = QtWidgets.QLabel(Form)
        self.minimo.setGeometry(QtCore.QRect(190, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(20)
        self.minimo.setFont(font)
        self.minimo.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(71, 94, 223);")
        self.minimo.setText("")
        self.minimo.setObjectName("minimo")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(270, 180, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(71, 94, 223);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(270, 220, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(71, 94, 223);")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(310, 180, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(310, 220, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(20)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(270, 270, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(71, 94, 223);")
        self.label_19.setObjectName("label_19")
        self.Resultado = QtWidgets.QLabel(Form)
        self.Resultado.setGeometry(QtCore.QRect(190, 270, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(20)
        self.Resultado.setFont(font)
        self.Resultado.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(71, 94, 223);")
        self.Resultado.setText("")
        self.Resultado.setObjectName("Resultado")
        self.btn_resultado = QtWidgets.QPushButton(Form)
        self.btn_resultado.setGeometry(QtCore.QRect(30, 270, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(20)
        self.btn_resultado.setFont(font)
        self.btn_resultado.setStyleSheet("background-color: rgb(49, 140, 120);\n"
"color: rgb(255, 255, 255);")
        self.btn_resultado.setObjectName("btn_resultado")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Tol_title.setText(_translate("Form", "Tolerancia:"))
        self.label_14.setText(_translate("Form", "Ω"))
        self.label_15.setText(_translate("Form", "Ω"))
        self.label_16.setText(_translate("Form", "máximo"))
        self.label_17.setText(_translate("Form", "mínimo"))
        self.label_19.setText(_translate("Form", "Ω"))
        self.btn_resultado.setText(_translate("Form", "Resultado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

