from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from random import randint
from PyQt5 import uic


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.point = [randint(50, 400), randint(50, 400)]
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.point = [randint(50, 400), randint(50, 400)]
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setBrush(QColor('yellow'))
        rad = randint(0, 100)
        painter.drawEllipse(self.point[0], self.point[1], rad, rad)


if __name__ == '__main__':
    app = QApplication([])
    w = Widget()
    w.show()
    app.exec()