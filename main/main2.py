import sys
import sqlite3

#типо импорт для интерфейса
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLineEdit, QLCDNumber,QLabel
from PyQt5.QtCore import QRect, Qt

now_id = None
class Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.destroy()
        self.close()

    def initUI(self) -> None:
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Start()
    ex.show()
    sys.exit(app.exec())