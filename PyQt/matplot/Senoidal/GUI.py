# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(715, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(500, 500))
        self.frame.setStyleSheet("background-color: rgb(74, 74, 74);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_grafica = QtWidgets.QVBoxLayout()
        self.verticalLayout_grafica.setObjectName("verticalLayout_grafica")
        self.horizontalLayout.addLayout(self.verticalLayout_grafica)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #FFFFFF;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.Slider1 = QtWidgets.QSlider(self.frame_2)
        self.Slider1.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #F78743;\n"
"    height: 4px;\n"
"    background: #F78743;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #2440D0;\n"
"    width: 10px; \n"
"    height:10px;\n"
"\n"
"    left: 11px; \n"
"    right: 11px;\n"
"\n"
"    margin: -12px;     \n"
"    border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"    background-color: white; \n"
"    border: 1px solid white;\n"
"}")
        self.Slider1.setOrientation(QtCore.Qt.Horizontal)
        self.Slider1.setObjectName("Slider1")
        self.verticalLayout_2.addWidget(self.Slider1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.Slider2 = QtWidgets.QSlider(self.frame_2)
        self.Slider2.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #F78743;\n"
"    height: 4px;\n"
"    background: #F78743;\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #2440D0;\n"
"    width: 10px; \n"
"    height:10px;\n"
"\n"
"    left: 11px; \n"
"    right: 11px;\n"
"\n"
"    margin: -12px;     \n"
"    border-radius: 4px;\n"
"\n"
"}\n"
"\n"
"QSlider::add-page:horizontal{\n"
"    background-color: white; \n"
"    border: 1px solid white;\n"
"}")
        self.Slider2.setOrientation(QtCore.Qt.Horizontal)
        self.Slider2.setObjectName("Slider2")
        self.verticalLayout_2.addWidget(self.Slider2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setStyleSheet("background-color: rgb(126, 43, 194);\n"
"color: #FFFFFF;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Variar Ampllitud y Frecuencia"))
        self.pushButton.setText(_translate("MainWindow", "Salir"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

'''