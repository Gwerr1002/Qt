from PyQt5.QtWidgets import QMainWindow,QPushButton, QApplication, QHBoxLayout, QWidget
from PyQt5.QtWidgets import QVBoxLayout,QGridLayout, QStackedLayout

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.render()
        self.componentDidMount()

    def render(self):
        self.layout = QStackedLayout() #QHBoxLayout()
        self.btn1 = QPushButton("Boton 1")
        self.btn2 = QPushButton("Boton 2")
        self.btn3 = QPushButton("Boton 3")

        for activity in [self.btn1, self.btn2, self.btn3]:
            self.layout.addWidget(activity)

        self.layout.setCurrentIndex(0)

        widget = QWidget(self)
        widget.setLayout(self.layout) #mostramos layout

        self.setCentralWidget(widget)

    def componentDidMount(self):
        self.btn1.clicked.connect(lambda x: self.switchLayout(1))
        self.btn2.clicked.connect(lambda x: self.switchLayout(2))
        self.btn3.clicked.connect(lambda x: self.switchLayout(0))

    def switchLayout(self, index):
        self.layout.setCurrentIndex(index)

if __name__ == '__main__':
    app = QApplication([])
    activity = App()
    activity.show()
    app.exec_()
