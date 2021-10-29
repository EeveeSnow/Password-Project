import sys
#типо импорт для интерфейса
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QStackedWidget
from PyQt5.QtWidgets import QLineEdit, QLCDNumber,QLabel
from PyQt5.QtCore import QRect, Qt

from registration_Ui import Ui_Reg
from login_Ui import Ui_Log

class UI_Start(QWidget):
    def __init__(self):
        super().__init__()

        self.layout2 = QVBoxLayout() 
        
        self.registerButton = QPushButton("Register", self)
        self.registerButton.setGeometry(QRect(250, 280, 170, 40))
        self.registerButton.clicked.connect(self.registr)

        self.loginButton = QPushButton("Login", self)
        self.loginButton.setGeometry(QRect(250, 380, 170, 40))
        self.loginButton.clicked.connect(self.loggin)

        
        self.layout2.addWidget(self.registerButton)
        self.layout2.addWidget(self.loginButton)
        self.setLayout(self.layout2)
    
    def registr(self):
        self.layout2.itemAt(0).widget().deleteLater()
        self.layout2.itemAt(1).widget().deleteLater()
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(Ui_Reg())
        self.layout2.addWidget(self.stackedWidget)
   
    def loggin(self):
        self.layout2.itemAt(0).widget().deleteLater()
        self.layout2.itemAt(1).widget().deleteLater()
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(Ui_Log())
        self.layout2.addWidget(self.stackedWidget)





# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     self = QtWidgets.QMainWindow()
#     ui = UI_Start()
#     ui.show()
#     sys.exit(app.exec_())