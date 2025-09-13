import sys
from datetime import datetime

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow, QApplication, QListWidgetItem

from uis.diary import Ui_MainWindow


class Diary(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add)

    def add(self):
        date = self.calendarWidget.selectedDate()
        time = self.timeEdit.time()
        item = QListWidgetItem(f"{date.toString("dd.MM.yyyy")}"
                                f" {time.toString("hh:mm")}\n{self.lineEdit.text()}")
        item.setFont(QFont("Ubuntu", 20, 20, False))
        item.dt = datetime.combine(date.toPyDate(), time.toPyTime()).timestamp()
        self.listWidget.addItem(item)
        self.sort()

    def sort(self):
        items = []
        while self.listWidget.count() != 0:
            items.append(self.listWidget.takeItem(0))
        items.sort(key=lambda x: x.dt)
        for item in items:
            self.listWidget.addItem(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Diary()
    ex.show()
    sys.exit(app.exec())