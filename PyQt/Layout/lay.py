from PyQt5.QtWidgets import QMainWindow,QPushButton, QApplication, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QVBoxLayout,QGridLayout, QStackedLayout

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.render()

    def render(self):
        layout = QGridLayout() #QHBoxLayout()
        btn1 = QPushButton("Boton 1")
        btn2 = QPushButton("Boton 2")
        btn3 = QPushButton("Boton 3")
        i,j = 0,0
        for widget in [btn1, btn2, btn3]:
            layout.addWidget(widget,i,j) #guardamos botones en el layout
            if i <= 1:
                i += 2
            else:
                i = 0
                j += 1

        widget = QWidget(self)
        widget.setLayout(layout) #mostramos layout

        self.setCentralWidget(widget)

if __name__ == '__main__':
    app = QApplication([])
    activity = App()
    activity.show()
    app.exec_()
