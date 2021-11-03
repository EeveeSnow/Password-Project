from supply.key_supply import MasterSupply
from supply.registration_supply import RegSupply
#типо импорт для интерфейса
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel, QMessageBox, QStackedWidget
from PyQt5 import uic

from storage_Ui import ui_storage

class Ui_Reg(QWidget):
    def __init__(self):
        super().__init__()

        self.layout2 = QVBoxLayout() 
        uic.loadUi("main/design/register.ui", self)
        self.loginButton.clicked.connect(self.registerHelp)
        self.setFixedSize(1300, 720)
        self.setLayout(self.layout2)


    def registerHelp(self):
        Password = self.passwordEdit.text()
        Nickname = self.loginEdit.text()
        Master = self.masterEdit.text()
        reg = RegSupply(Nickname, Password, Master)
        master = MasterSupply(Master)
        if not(reg.cheack()[0]):
            self.Error_PopUp(reg.cheack()[1])
        else:
            if not(master.cheack()[0]):
                self.Error_PopUp(master.cheack()[1])
            else:
                idn = reg.add()
                reg.creator()
                open("main/local/user.txt", "w").write(str(idn))
                self.stackedWidget = QStackedWidget()
                self.stackedWidget.addWidget(ui_storage())
                self.layout2.addWidget(self.stackedWidget)
                uic.loadUi(None)

    def Error_PopUp(self, error):
        popup = QMessageBox()
        popup.setWindowTitle("Error")
        popup.setText(error)
        popup.exec_()
