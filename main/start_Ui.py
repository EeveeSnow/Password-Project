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
        self.layout2 = QVBoxLayout() 
        
        self.registerButton.clicked.connect(self.registr)

        self.loginButton.clicked.connect(self.loggin)

        self.setLayout(self.layout2)
    
    def registr(self):
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(Ui_Reg())
        self.layout2.addWidget(self.stackedWidget)
   
    def loggin(self):
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(Ui_Log())
        self.layout2.addWidget(self.stackedWidget)





# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     self = QtWidgets.QMainWindow()
#     ui = UI_Start()
#     ui.show()
#     sys.exit(app.exec_())