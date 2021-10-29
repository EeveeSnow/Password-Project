
from supply.registration_supply import RegSupply
#типо импорт для интерфейса
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import QRect, Qt

class Ui_Reg(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout() 
        self.resize(1280, 720)   

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
      
        layout.addWidget(self.Nickname)
        layout.addWidget(self.Password)
        layout.addWidget(self.registerButton)
        
        self.setLayout(layout)

        # QtCore.QMetaObject.connectSlotsByName(Reg)

    def registerHelp(self):
        Password = self.Nickname.text()
        Nickname = self.Password.text()
        reg = RegSupply(Nickname, Password)
        if not(reg.cheack()[0]):
            reg.add()
        else:
            reg.add()


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     Reg = QtWidgets.QMainWindow()
#     ui = Ui_Reg()
#     ui.setupUI(Reg)
#     Reg.show()
#     sys.exit(app.exec_())