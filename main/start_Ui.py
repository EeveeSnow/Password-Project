import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

from design.start import Ui_Form
from login_Ui import Ui_Log
from registration_Ui import Ui_Reg


class UI_Start(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Password hundler")
        self.registerButton.clicked.connect(self.registr)
        self.loginButton.clicked.connect(self.login)
    
    def registr(self):
        self.reg = Ui_Reg()
        self.reg.show()
        self.hide()
        return 1

   
    def login(self):
        self.log = Ui_Log()
        self.log.show()
        self.hide()
        return 2
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    self = QMainWindow()
    ui = UI_Start()
    ui.show()
    sys.exit(app.exec_())
