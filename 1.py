import sys

from PyQt6.QtGui import QColor, QPen, QBrush
from PyQt6.QtWidgets import QMainWindow, QApplication, QGraphicsScene
from PyQt6.QtCore import Qt
from PyQt6 import uic

class Flag(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("uis/flag.ui", self)
        self.rButtons = [[self.r1, self.r2, self.r3, self.r4, self.r5],
                        [self.r6, self.r7, self.r8, self.r9, self.r10],
                        [self.r11, self.r12, self.r13, self.r14, self.r15]]
        self.colors = [QColor(Qt.GlobalColor.white),
                        QColor(Qt.GlobalColor.green),
                        QColor(Qt.GlobalColor.blue),
                        QColor(Qt.GlobalColor.red),
                        QColor(Qt.GlobalColor.yellow)]
        self.colorNames = ["Белый", "Зеленый", "Синий", "Красный", "Желтый"]
        self.scene = QGraphicsScene()
        self.lines = []
        for i in range(3):
            rect = self.scene.addRect(0, i * 50, 350, 50, pen=QPen(Qt.GlobalColor.transparent))
            self.lines.append(rect)
        for i, column in enumerate(self.rButtons):
            for j, button in enumerate(column):
                button.line = self.lines[i]
                button.color = self.colors[j]
                button.colorName = self.colorNames[j]
                button.clicked.connect(self.changeColor)
                if j == 0:
                    button.click()
        self.drawButton.clicked.connect(self.draw)
        self.graphicsView.setScene(self.scene)

    def changeColor(self):
        button = self.sender()
        button.line.color = button.color
        button.line.colorName = button.colorName

    def draw(self):
        for line in self.lines:
            line.setBrush(QBrush(line.color))
        self.label.setText(", ".join([line.colorName for line in self.lines]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Flag()
    ex.show()
    sys.exit(app.exec())