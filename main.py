import random
import sys

from PyQt5 import uic
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPolygon, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.coords = []
        self.qp = QPainter()
        self.flag = False
        self.statue = None
        self.startbtn.clicked.connect(self.star)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.setBrushColor()
            self.draw(self.status)
            self.qp.end()

    def setBrushColor(self):
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.qp.setBrush(QColor(255, 179, 0))

    def draw(self, status):
        self.size = random.randint(10, 100)
        self.qp.drawEllipse(*self.coords, self.size, self.size)

    def initUi(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Рисование')
        self.show()

    def star(self):
        self.coords = [10, 10]
        self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())