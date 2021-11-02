from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QStackedWidget,
    QMainWindow
)
from PyQt5.QtCore import QRect, Qt
import sys

from start_Ui import UI_Start
from storage_Ui import ui_storage

class Hundler(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password hundler")
        self.setFixedSize(1280, 720)
        idn = open("main/local/user.txt", "r").read()
        mainlayout = QVBoxLayout()     

        self.stackedWidget = QStackedWidget()
        if idn == "":
            self.stackedWidget.addWidget(UI_Start())
            self.show()
        else:
            self.storage = ui_storage()
            self.storage.show()

        mainlayout.addWidget(self.stackedWidget)

        self.setLayout(mainlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hundler = Hundler()
    sys.exit(app.exec_()) 