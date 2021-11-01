from supply.key_supply import MasterSupply
from supply.registration_supply import RegSupply
#типо импорт для интерфейса
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel, QMessageBox, QStackedWidget
from PyQt5.QtCore import QRect, Qt

from storage_Ui import ui_storage

class Ui_Reg(QWidget):
    def __init__(self):
        super().__init__()

        self.layout2 = QVBoxLayout() 
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
      
        self.layout2.addWidget(self.Nickname)
        self.layout2.addWidget(self.Password)
        self.layout2.addWidget(self.Master)
        self.layout2.addWidget(self.registerButton)
        
        self.setLayout(self.layout2)

        # QtCore.QMetaObject.connectSlotsByName(Reg)

    def registerHelp(self):
        Password = self.Nickname.text()
        Nickname = self.Password.text()
        Master = self.Master.text()
        reg = RegSupply(Nickname, Password, Master)
        master = MasterSupply(Master)
        if not(reg.cheack()[0]):
            self.Error_PopUp(reg.cheack()[1])
        else:
            if not(master.cheack()[0]):
                self.Error_PopUp(master.cheack()[1])
            else:
                reg.add()
                self.layout2.itemAt(0).widget().deleteLater()
                self.layout2.itemAt(1).widget().deleteLater()
                self.layout2.itemAt(2).widget().deleteLater()
                self.layout2.itemAt(3).widget().deleteLater()
                self.stackedWidget = QStackedWidget()
                self.stackedWidget.addWidget(ui_storage())
                self.layout2.addWidget(self.stackedWidget)
    
    def Error_PopUp(self, error):
        popup = QMessageBox()
        popup.setWindowTitle("Error")
        popup.setText(error)
        x = popup.exec_()

# class Ui_Error(QWidget):
#     def __init__(self, error):
#         super().__init__()
#         info = error
#         self.layout2 = QVBoxLayout() 
#         self.resize(300, 200)
#         message = QLabel(self)
#         message.setText(info)
#         self.layout2.addWidget(message)
#         self.setLayout(self.layout2)
