import sys

from PyQt6.QtWidgets import QMainWindow, QApplication

from uis.notebook import Ui_MainWindow


class Notebook(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.addContact)
        self.addButton.setEnabled(False)
        self.name.textChanged.connect(self.changeButtonState)
        self.number.textChanged.connect(self.changeButtonState)

    def addContact(self):
        self.listWidget.addItem(f"{self.number.text()}\n{self.name.text()}")

    def changeButtonState(self):
        if self.isContactCorrect():
            self.addButton.setEnabled(True)
        else:
            self.addButton.setEnabled(False)

    def isContactCorrect(self):
        return (len(self.number.text()) == 19 and not "_" in self.number.text()) and len(self.name.text()) > 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Notebook()
    ex.show()
    sys.exit(app.exec())