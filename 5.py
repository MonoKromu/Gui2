import difflib
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from uis.anti import Ui_MainWindow


class AntiPlagiat(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.compare)

    def compare(self):
        similarity = difflib.SequenceMatcher(None, self.plainTextEdit.toPlainText(), self.plainTextEdit_2.toPlainText()).ratio() * 100
        if similarity > self.doubleSpinBox.value():
            self.statusbar.setStyleSheet("QStatusBar { background-color: #ff0000; color: #000000; font-size: 15pt; }")
        else:
            self.statusbar.setStyleSheet("QStatusBar { background-color: #32CD32; color: #000000; font-size: 15pt; }")
        self.statusbar.showMessage(str(round(similarity, 3)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AntiPlagiat()
    ex.show()
    sys.exit(app.exec())