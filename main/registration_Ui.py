import sys
from supply.registration_supply import RegSupply
#типо импорт для интерфейса
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLineEdit, QLCDNumber,QLabel
from PyQt5.QtCore import QRect, Qt

class Ui_Reg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):       
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
    
    def registerHelp(self):
        Nickname = self.Nickname.text()
        Password = self.Password.text()
        reg = RegSupply(Nickname, Password)
        if not(reg.cheack()[0]):
            reg.add()
        else:
            reg.add()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Reg()
    ex.show()
    sys.exit(app.exec())