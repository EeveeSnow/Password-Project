from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QWidget, QStackedWidget, QApplication, QMainWindow
from PyQt5.QtCore import Qt
from registration_Ui import Ui_Reg
from login_Ui import Ui_Log

class UI_Start(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main/design/start.ui", self)
        self.registerButton.clicked.connect(self.registr)
        self.loginButton.clicked.connect(self.login)
    
    def registr(self):
        self.reg = Ui_Reg()
        self.reg.show()
        print("OK")
        self.hide()
        return 1

   
    def login(self):
        self.log = Ui_Log()
        self.log.show()
        print("OK")
        self.hide()
        return 2
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    self = QMainWindow()
    ui = UI_Start()
    ui.show()
    sys.exit(app.exec_())