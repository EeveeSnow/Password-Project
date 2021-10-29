import sys
#типо импорт для интерфейса
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLineEdit, QLCDNumber,QLabel
from PyQt5.QtCore import QRect, Qt

class UI_Start(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI(self)


    def setupUI(self, start):
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")


        self.registerButton = QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QRect(250, 280, 170, 40))
        self.registerButton.setText("Registeration")
        self.registerButton.clicked.connect(self.registr)

        self.registerButton = QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QRect(250, 380, 170, 40))
        self.registerButton.setText("Loggin")
        self.registerButton.clicked.connect(self.loggin)
        
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def registr(self):
        pass
    
    def loggin(self):
        pass



# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     self = QtWidgets.QMainWindow()
#     ui = UI_Start()
#     ui.setupUI(self)
#     self.show()
#     sys.exit(app.exec_())