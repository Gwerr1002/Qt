# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 21:14:50 2022

@author: gerard
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigCanvas, NavigationToolbar2QT as Toolbar
from PyQt5.QtWidgets import QApplication, QWidget

class Canvas(FigCanvas):
    def __init__(self, parent):
        fig, self.ax = plt.subplots(figsize = (5,4), dpi = 100)
        super().__init__(fig)
        self.setParent(parent)
        
        t = np.arange(0.0,2.0,0.01)
        s = 1 + np.sin(2*np.pi*t)
        self.ax.plot(t,s)
        self.ax.set(xlabel = 'time (s)', ylabel = 'mV',title = "About as it gets folks")
        self.ax.grid()
        
class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600, 800)
        
        chart = Canvas(self)
        
app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())
