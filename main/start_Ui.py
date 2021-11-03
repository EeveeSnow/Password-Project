import sys
#типо импорт для интерфейса
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QStackedWidget
from PyQt5.QtWidgets import QLineEdit, QLCDNumber,QLabel
from PyQt5.QtCore import QRect, Qt

from registration_Ui import Ui_Reg
from login_Ui import Ui_Log

class UI_Start(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main/design/start.ui", self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.registerButton.clicked.connect(self.registr)

        self.loginButton.clicked.connect(self.loggin)
    
    def registr(self):
        self.mainlayout.itemAt(0).layout().deleteLater()
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.resize(1280, 720)
        self.stackedWidget.addWidget(Ui_Reg())
        self.mainlayout.addWidget(self.stackedWidget)
        print("OK")
   
    def loggin(self):
        self.mainlayout.itemAt(0).layout().deleteLater()
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.resize(1280, 720)
        self.stackedWidget.addWidget(Ui_Log())
        self.mainlayout.addWidget(self.stackedWidget)
        uic.loadUi("main/design/popipo.ui")
        print("OK")
        





# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     self = QtWidgets.QMainWindow()
#     ui = UI_Start()
#     ui.show()
#     sys.exit(app.exec_())