import sys
from supply.registration_supply import RegSupply
#типо импорт для интерфейса
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLineEdit, QLCDNumber,QLabel
from PyQt5.QtCore import QRect, Qt

class Ui_Reg(QWidget):
    def setupUI(self, Reg):       
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
        self.registerButton.setText("Register")
        self.registerButton.clicked.connect(self.registerHelp)

        QtCore.QMetaObject.connectSlotsByName(Reg)

    def registerHelp(self):
        Password = self.Nickname.text()
        Nickname = self.Password.text()
        reg = RegSupply(Nickname, Password)
        if not(reg.cheack()[0]):
            reg.add()
        else:
            reg.add()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Reg = QtWidgets.QMainWindow()
    ui = Ui_Reg()
    ui.initUI(Reg)
    Reg.show()
    sys.exit(app.exec_())