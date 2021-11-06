import sys
from supply.login_supply import LogSupply
#типо импорт для интерфейса
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QMainWindow
from PyQt5.QtCore import QRect, Qt

from storage_Ui import ui_storage

class Ui_Log(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main/design/login.ui", self)
        self.logButton.clicked.connect(self.registerHelp)
    
    def registerHelp(self):
        Password = self.pasEdit.text()
        Nickname = self.logEdit.text()
        log = LogSupply(Nickname, Password)
        idn = log.cheack()
        if idn != -1:
            open("main/local/user.txt", "w").write(str(idn))
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