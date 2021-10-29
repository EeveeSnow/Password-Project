import sys
from supply.loggin_supply import LogSupply
#типо импорт для интерфейса
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget
from PyQt5.QtWidgets import QLineEdit, QLCDNumber,QLabel
from PyQt5.QtCore import QRect, Qt

class Ui_Log(QWidget):
    def setupUI(self, Log):       
        self.Nickname = QLineEdit(self)
        self.Nickname.setGeometry(QRect(230, 220, 170, 30))
        self.Nickname.setInputMethodHints(Qt.ImhHiddenText)
        self.Nickname.setObjectName("Nickname")

        self.Password = QLineEdit(self)
        self.Password.setGeometry(QRect(230, 170, 170, 30))
        self.Password.setAutoFillBackground(False)
        self.Password.setObjectName("Password")

        self.registerButton = QPushButton(self)
        self.registerButton.setGeometry(QRect(230, 280, 170, 40))
        self.registerButton.setText("Loggin")
        self.registerButton.clicked.connect(self.registerHelp)
        
        QtCore.QMetaObject.connectSlotsByName(Log)
    
    def registerHelp(self):
        Password = self.Nickname.text()
        Nickname = self.Password.text()
        log = LogSupply(Nickname, Password)
        id = log.cheack()
        if id != -1:
            print("OK")
        else:
            print("NO")

            

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     Log = QtWidgets.QMainWindow()
#     ui = Ui_Log()
#     ui.initUI(Log)
#     Log.show()
#     sys.exit(app.exec_())