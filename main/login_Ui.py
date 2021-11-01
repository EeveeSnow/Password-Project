import sys
from supply.login_supply import LogSupply
#типо импорт для интерфейса
from PyQt5.QtWidgets import QPushButton, QWidget, QLineEdit, QVBoxLayout, QStackedWidget, QMessageBox
from PyQt5.QtCore import QRect, Qt

from storage_Ui import ui_storage


class Ui_Log(QWidget):
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

        self.registerButton = QPushButton(self)
        self.registerButton.setGeometry(QRect(230, 280, 170, 40))
        self.registerButton.setText("Loggin")
        self.registerButton.clicked.connect(self.registerHelp)
        
        
        self.layout2.addWidget(self.Nickname)
        self.layout2.addWidget(self.Password)
        self.layout2.addWidget(self.registerButton)
        
        self.setLayout(self.layout2)
    
    def registerHelp(self):
        Password = self.Nickname.text()
        Nickname = self.Password.text()
        log = LogSupply(Nickname, Password)
        id = log.cheack()
        if id != -1:
            self.layout2.itemAt(0).widget().deleteLater()
            self.layout2.itemAt(1).widget().deleteLater()
            self.layout2.itemAt(2).widget().deleteLater()
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