import sys

#типо импорт для интерфейса
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from design.login import Ui_Form
from storage_Ui import ui_storage
from supply.login_supply import LogSupply


class Ui_Log(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Password hundler")
        self.logButton.clicked.connect(self.registerHelp)
    
    def registerHelp(self):
        Password = self.passwordEdit.text()
        Nickname = self.loginEdit.text()
        log = LogSupply(Nickname, Password)
        idn = log.cheack()
        if idn != -1:
            open("local/user.txt", "w").write(str(idn))
            self.storage = ui_storage()
            self.storage.show()
            self.hide()
        else:
            self.Error_PopUp("Wrong login or password")
    
    def Error_PopUp(self, error):
        popup = QMessageBox()
        popup.setWindowTitle("Error")
        popup.setText(error)
        popup.exec_()

            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Log = QMainWindow()
    ui = Ui_Log()
    Log.show()
    sys.exit(app.exec_())
