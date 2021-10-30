from supply.key_supply import MasterSupply
from supply.registration_supply import RegSupply
#типо импорт для интерфейса
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
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

        self.Master = QLineEdit(self)
        self.Master.setGeometry(QRect(230, 170, 170, 30))
        self.Master.setAutoFillBackground(False)
        self.Master.setObjectName("Master")

        self.registerButton = QPushButton(self)
        self.registerButton.setGeometry(QRect(230, 280, 170, 40))
        self.registerButton.setText("Register")
        self.registerButton.clicked.connect(self.registerHelp)
      
        layout.addWidget(self.Nickname)
        layout.addWidget(self.Password)
        layout.addWidget(self.Master)
        layout.addWidget(self.registerButton)
        
        self.setLayout(layout)

        # QtCore.QMetaObject.connectSlotsByName(Reg)

    def registerHelp(self):
        Password = self.Nickname.text()
        Nickname = self.Password.text()
        Master = self.Master.text()
        reg = RegSupply(Nickname, Password, Master)
        master = MasterSupply(Master)
        if not(reg.cheack()[0]):
            Ui_Error(reg.cheack()[1]).show()
        else:
            if not(master.cheack()[0]):
                Ui_Error(master.cheack()[1]).show()
            else:
                reg.add()

class Ui_Error(QWidget):
    def __init__(self, error):
        super().__init__()
        info = error
        layout = QVBoxLayout() 
        self.resize(300, 200)
        message = QLabel(self)
        message.setText(info)
        layout.addWidget(message)
        self.setLayout(layout)



# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     Reg = QtWidgets.QMainWindow()
#     ui = Ui_Reg()
#     ui.setupUI(Reg)
#     Reg.show()
#     sys.exit(app.exec_())