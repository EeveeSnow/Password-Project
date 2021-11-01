import sys
from supply.login_supply import LogSupply
#типо импорт для интерфейса
from PyQt5 import uic
from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QVBoxLayout, QStackedWidget, QMessageBox
from PyQt5.QtCore import QRect, Qt

from storage_Ui import ui_storage


class Ui_Log(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main/design/login.ui", self)
        self.layout2 = QVBoxLayout() 

        self.loginButton.clicked.connect(self.registerHelp)
        
        self.setLayout(self.layout2)
    
    def registerHelp(self):
        Password = self.passwordEdit.text()
        Nickname = self.loginEdit.text()
        log = LogSupply(Nickname, Password)
        id = log.cheack()
        if id != -1:
            self.stackedWidget = QStackedWidget()
            self.stackedWidget.addWidget(ui_storage())
            self.layout2.addWidget(self.stackedWidget)
        else:
            self.Error_PopUp("Wrong login or password")
    
    def Error_PopUp(self, error):
        popup = QMessageBox()
        popup.setWindowTitle("Error")
        popup.setText(error)
        x = popup.exec_()

            

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     Log = QtWidgets.QMainWindow()
#     ui = Ui_Log()
#     ui.initUI(Log)
#     Log.show()
#     sys.exit(app.exec_())