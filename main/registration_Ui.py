import sys

from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMessageBox,
                             QVBoxLayout, QWidget)
from design.register import Ui_Form
from storage_Ui import ui_storage
from supply.key_supply import MasterSupply
from supply.registration_supply import RegSupply


class Ui_Reg(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Password hundler")
        self.layout2 = QVBoxLayout()
        self.loginButton.clicked.connect(self.registerHelp)

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
                self.storage = ui_storage()
                self.storage.show()
                self.hide()

    def Error_PopUp(self, error):
        popup = QMessageBox()
        popup.setWindowTitle("Error")
        popup.setText(error)
        popup.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    self = QMainWindow()
    ui = Ui_Reg()
    ui.show()
    sys.exit(app.exec_())
