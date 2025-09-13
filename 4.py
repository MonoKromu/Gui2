import sys
import random
from time import sleep

from PyQt6.QtWidgets import QApplication, QMainWindow, QLCDNumber

from uis.pseudonim import Ui_MainWindow


class Game(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.playerTurn)
        self.pushButton_2.clicked.connect(self.restart)
        self.restart()

    def restart(self):
        self.listWidget.clear()
        self.pushButton.setEnabled(False)
        self.lcdNumber.display(random.randint(10, 30))
        self.updateHistory(f"Всего камней: {self.lcdNumber.intValue()}")
        if random.choice([1, 0]):
            self.updateHistory("Игра началась. Первым ходит игрок")
            self.pushButton.setEnabled(True)
        else:
            self.updateHistory("Игра началась. Первым ходит ИИ")

            self.aiTurn()

    def playerTurn(self):
        self.pushButton.setEnabled(False)
        self.spinBox.setMaximum(3)
        self.lcdNumber.display(self.lcdNumber.intValue() - self.spinBox.value())
        if self.lcdNumber.intValue() == 0:
            self.updateHistory("Игрок победил!")
            self.pushButton.setEnabled(False)
        else:
            self.updateHistory(f"Игрок взял камни ({self.spinBox.value()}). Ходит ИИ")
            self.aiTurn()

    def aiTurn(self):
        value = self.lcdNumber.intValue()
        rem = value % 4
        if rem == 0:
            rocks = random.randint(1, 3)
        else:
            rocks = rem
        new_value = value - rocks
        self.lcdNumber.display(new_value)
        if new_value == 0:
            self.updateHistory("ИИ победил!")
        else:
            if new_value < 3:
                self.spinBox.setMaximum(new_value)
            self.updateHistory(f"ИИ взял камни ({rocks}). Ходит игрок")
            self.pushButton.setEnabled(True)

    def updateHistory(self, action: str):
        self.listWidget.addItem(action)
        self.listWidget.scrollToBottom()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Game()
    ex.show()
    sys.exit(app.exec())