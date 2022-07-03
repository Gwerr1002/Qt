# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesignerGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Resources.Canvas import QMatplotlibCanvas as Qcanvas
import Resources.logo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 700)
        MainWindow.setMinimumSize(QtCore.QSize(850, 700))
        MainWindow.setStyleSheet("background-color: rgb(18, 24, 39);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 85, 0);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Tfiltro = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Tfiltro.setFont(font)
        self.Tfiltro.setStyleSheet("color: rgb(140, 129, 255);")
        self.Tfiltro.setObjectName("Tfiltro")
        self.Tfiltro.addItem("")
        self.Tfiltro.addItem("")
        self.Tfiltro.addItem("")
        self.Tfiltro.addItem("")
        self.Tfiltro.setItemText(3, "")
        self.verticalLayout.addWidget(self.Tfiltro)
        self.HP = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setBold(True)
        font.setWeight(75)
        self.HP.setFont(font)
        self.HP.setStyleSheet("color: rgb(140, 129, 255);")
        self.HP.setObjectName("HP")
        self.verticalLayout.addWidget(self.HP)
        self.IIR = QtWidgets.QCheckBox(self.frame)
        self.IIR.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setBold(True)
        font.setWeight(75)
        self.IIR.setFont(font)
        self.IIR.setStyleSheet("color: rgb(140, 129, 255);")
        self.IIR.setObjectName("IIR")
        self.verticalLayout.addWidget(self.IIR)
        self.Ap_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Ap_label.setFont(font)
        self.Ap_label.setStyleSheet("color: rgb(255, 126, 14);")
        self.Ap_label.setObjectName("Ap_label")
        self.verticalLayout.addWidget(self.Ap_label)
        self.Ap = QtWidgets.QDoubleSpinBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Ap.setFont(font)
        self.Ap.setStyleSheet("color: rgb(140, 129, 255);")
        self.Ap.setPrefix("")
        self.Ap.setDecimals(3)
        self.Ap.setMinimum(1.0)
        self.Ap.setMaximum(1000000000000.0)
        self.Ap.setObjectName("Ap")
        self.verticalLayout.addWidget(self.Ap)
        self.Ar_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Ar_label.setFont(font)
        self.Ar_label.setStyleSheet("color: rgb(255, 126, 14);")
        self.Ar_label.setObjectName("Ar_label")
        self.verticalLayout.addWidget(self.Ar_label)
        self.Ar = QtWidgets.QDoubleSpinBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Ar.setFont(font)
        self.Ar.setStyleSheet("color: rgb(140, 129, 255);")
        self.Ar.setDecimals(3)
        self.Ar.setMinimum(1.0)
        self.Ar.setMaximum(1000000000000.0)
        self.Ar.setObjectName("Ar")
        self.verticalLayout.addWidget(self.Ar)
        self.fp_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fp_label.setFont(font)
        self.fp_label.setStyleSheet("color: rgb(255, 126, 14);")
        self.fp_label.setObjectName("fp_label")
        self.verticalLayout.addWidget(self.fp_label)
        self.fp = QtWidgets.QDoubleSpinBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fp.setFont(font)
        self.fp.setStyleSheet("color: rgb(140, 129, 255);")
        self.fp.setDecimals(3)
        self.fp.setMinimum(1.0)
        self.fp.setMaximum(1000000000000.0)
        self.fp.setObjectName("fp")
        self.verticalLayout.addWidget(self.fp)
        self.fr_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fr_label.setFont(font)
        self.fr_label.setStyleSheet("color: rgb(255, 126, 14);")
        self.fr_label.setObjectName("fr_label")
        self.verticalLayout.addWidget(self.fr_label)
        self.fr = QtWidgets.QDoubleSpinBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fr.setFont(font)
        self.fr.setStyleSheet("color: rgb(140, 129, 255);")
        self.fr.setDecimals(3)
        self.fr.setMinimum(1.0)
        self.fr.setMaximum(1000000000000.0)
        self.fr.setObjectName("fr")
        self.verticalLayout.addWidget(self.fr)
        self.fs_label = QtWidgets.QLabel(self.frame)
        self.fs_label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fs_label.setFont(font)
        self.fs_label.setStyleSheet("color: rgb(255, 126, 14);")
        self.fs_label.setObjectName("fs_label")
        self.verticalLayout.addWidget(self.fs_label)
        self.fs = QtWidgets.QDoubleSpinBox(self.frame)
        self.fs.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fs.setFont(font)
        self.fs.setStyleSheet("color: rgb(140, 129, 255);")
        self.fs.setDecimals(3)
        self.fs.setMinimum(1.0)
        self.fs.setMaximum(1000000000000.0)
        self.fs.setObjectName("fs")
        self.verticalLayout.addWidget(self.fs)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.GenFiltro = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.GenFiltro.setFont(font)
        self.GenFiltro.setStyleSheet("border-color: rgb(0, 35, 107);\n"
"color: rgb(110, 209, 255);")
        self.GenFiltro.setObjectName("GenFiltro")
        self.verticalLayout.addWidget(self.GenFiltro)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color: rgb(140, 129, 255);")
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Tab1 = QtWidgets.QWidget()
        self.Tab1.setObjectName("Tab1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Tab1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Mag_frame = QtWidgets.QFrame(self.Tab1)
        self.Mag_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Mag_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mag_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mag_frame.setObjectName("Mag_frame")
        self.verticalLayout_5.addWidget(self.Mag_frame)
        
        self.gridLayout_1 = QtWidgets.QGridLayout(self.Mag_frame)
        self.gridLayout_1.setObjectName("gridLayout")
        self.MagCanvas = Qcanvas(self.Mag_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MagCanvas.sizePolicy().hasHeightForWidth())
        self.MagCanvas.setSizePolicy(sizePolicy)
        self.MagCanvas.setObjectName("matplotlibCanvas")
        self.gridLayout_1.addWidget(self.MagCanvas, 0, 0, 1, 1)
        
        self.tabWidget.addTab(self.Tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Phase_frame = QtWidgets.QFrame(self.tab2)
        self.Phase_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Phase_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Phase_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Phase_frame.setObjectName("Phase_frame")
        self.verticalLayout_6.addWidget(self.Phase_frame)
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Phase_frame)
        self.gridLayout_2.setObjectName("gridLayout")
        self.PhaseCanvas = Qcanvas(self.Phase_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PhaseCanvas.sizePolicy().hasHeightForWidth())
        self.PhaseCanvas.setSizePolicy(sizePolicy)
        self.PhaseCanvas.setObjectName("matplotlibCanvas")
        self.gridLayout_2.addWidget(self.PhaseCanvas, 0, 0, 1, 1)
        
        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Nyquist_frame = QtWidgets.QFrame(self.tab3)
        self.Nyquist_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Nyquist_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Nyquist_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Nyquist_frame.setObjectName("Nyquist_frame")
        self.verticalLayout_7.addWidget(self.Nyquist_frame)
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Nyquist_frame)
        self.gridLayout_3.setObjectName("gridLayout")
        self.NyCanvas = Qcanvas(self.Nyquist_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NyCanvas.sizePolicy().hasHeightForWidth())
        self.NyCanvas.setSizePolicy(sizePolicy)
        self.NyCanvas.setObjectName("matplotlibCanvas")
        self.gridLayout_3.addWidget(self.NyCanvas, 0, 0, 1, 1)
        
        self.tabWidget.addTab(self.tab3, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 126, 14);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.Ap_slider = QtWidgets.QSlider(self.frame_2)
        self.Ap_slider.setMinimum(1)
        self.Ap_slider.setMaximum(100)
        self.Ap_slider.setSliderPosition(50)
        self.Ap_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Ap_slider.setObjectName("Ap_slider")
        self.verticalLayout_3.addWidget(self.Ap_slider)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 126, 14);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.Ar_slider = QtWidgets.QSlider(self.frame_2)
        self.Ar_slider.setMinimum(1)
        self.Ar_slider.setMaximum(100)
        self.Ar_slider.setSliderPosition(50)
        self.Ar_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Ar_slider.setObjectName("Ar_slider")
        self.verticalLayout_3.addWidget(self.Ar_slider)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 126, 14);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.fp_slider = QtWidgets.QSlider(self.frame_2)
        self.fp_slider.setMinimum(0)
        self.fp_slider.setMaximum(1000)
        self.fp_slider.setSliderPosition(500)
        self.fp_slider.setOrientation(QtCore.Qt.Horizontal)
        self.fp_slider.setObjectName("fp_slider")
        self.verticalLayout_3.addWidget(self.fp_slider)
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 126, 14);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.fr_slider = QtWidgets.QSlider(self.frame_2)
        self.fr_slider.setMinimum(0)
        self.fr_slider.setMaximum(1000)
        self.fr_slider.setSliderPosition(500)
        self.fr_slider.setOrientation(QtCore.Qt.Horizontal)
        self.fr_slider.setObjectName("fr_slider")
        self.verticalLayout_3.addWidget(self.fr_slider)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("color: rgb(110, 209, 255);\n"
"background-color: rgb(46, 55, 72);\n"
"border-color: rgb(255, 0, 0);")
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.setStretch(0, 5)
        self.verticalLayout_4.setStretch(1, 2)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Filter Studio", "Filter Studio"))
        MainWindow.setWindowIcon(QtGui.QIcon(":logo/igun.png"))
        self.label.setText(_translate("MainWindow", "Seleccione el tipo de filtro"))
        self.Tfiltro.setItemText(0, _translate("MainWindow", "FIR"))
        self.Tfiltro.setItemText(1, _translate("MainWindow", "Butterworth"))
        self.Tfiltro.setItemText(2, _translate("MainWindow", "Chebyshev"))
        self.HP.setText(_translate("MainWindow", "HP"))
        self.IIR.setText(_translate("MainWindow", "IIR"))
        self.Ap_label.setText(_translate("MainWindow", "Ap"))
        self.Ap.setSuffix(_translate("MainWindow", " dB"))
        self.Ar_label.setText(_translate("MainWindow", "Ar"))
        self.Ar.setSuffix(_translate("MainWindow", " dB"))
        self.fp_label.setText(_translate("MainWindow", "fp"))
        self.fp.setSuffix(_translate("MainWindow", " hz"))
        self.fr_label.setText(_translate("MainWindow", "fr"))
        self.fr.setSuffix(_translate("MainWindow", " hz"))
        self.fs_label.setText(_translate("MainWindow", "fs"))
        self.fs.setSuffix(_translate("MainWindow", " hz"))
        self.GenFiltro.setText(_translate("MainWindow", "Generar diseño"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab1), _translate("MainWindow", "Magnitud"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Fase"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("MainWindow", "Nyquist"))
        self.label_7.setText(_translate("MainWindow", "Ap"))
        self.label_8.setText(_translate("MainWindow", "Ar"))
        self.label_11.setText(_translate("MainWindow", "fp"))
        self.label_12.setText(_translate("MainWindow", "fr"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Secciones del filtro"))
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