from supply.key_supply import MasterSupply
from supply.registration_supply import RegSupply
#типо импорт для интерфейса
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QApplication, QMainWindow
from PyQt5 import uic
import sys

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
                self.storage = ui_storage()
                self.storage.show()

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