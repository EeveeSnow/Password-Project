from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QStackedWidget,
    QPushButton,
)
from PyQt5.QtCore import QRect, Qt
import sys

from start_Ui import UI_Start
from registration_Ui import Ui_Reg
from login_Ui import Ui_Log

class Hundler(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password hundler")
        self.resize(1280, 720)

        mainlayout = QVBoxLayout()     

        self.stackedWidget = QStackedWidget()

        self.stackedWidget.addWidget(UI_Start())
        
        mainlayout.addWidget(self.stackedWidget)

        self.setLayout(mainlayout)
    
app = QApplication(sys.argv)
hundler = Hundler()
hundler.show()
sys.exit(app.exec_()) 

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     self = QMainWindow()
#     hundler = Hundler()
#     hundler.show()
#     sys.exit(app.exec())