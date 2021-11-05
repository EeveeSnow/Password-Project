from PyQt5.QtWidgets import QApplication, QWidget
import sys

from start_Ui import UI_Start
from registration_Ui import Ui_Reg
from login_Ui import Ui_Log
from storage_Ui import ui_storage

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QStackedWidget
import sys

from start_Ui import UI_Start
from registration_Ui import Ui_Reg
from login_Ui import Ui_Log


class Hundler(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password hundler")
        mainlayout = QVBoxLayout()     
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.resize(1400, 720)
        self.stackedWidget.setWindowTitle("Password hundler")
        # QWidget.statusBar(self).setVisible(False)
        idn = open("main/local/user.txt", "r").read()
        if idn == "":
            # pagew = open("main/local/page.txt", "w")
            # pagew.write('0')
            # pagew.close()
            n = 0
        else:
            # pagew = open("main/local/page.txt", "w")
            # pagew.write('3')
            # pagew.close()
            n = 3
        start = UI_Start()
        self.stackedWidget.addWidget(start)
        self.stackedWidget.addWidget(ui_storage())

        # pager = open("main/local/page.txt", "r")
        # n = int(pager.read()) 
        self.stackedWidget.setCurrentIndex(1)
        mainlayout.addWidget(self.stackedWidget)
        self.setLayout(mainlayout)
        if n == 0:
            n = start.login()
            self.stackedWidget.setCurrentIndex(n)

app = QApplication(sys.argv)
hundler = Hundler()
hundler.show()
sys.exit(app.exec_())

# app = QApplication(sys.argv)
# stackedWidget = QStackedWidget()
# stackedWidget.setFixedSize(1280, 720)
# stackedWidget.setWindowTitle("Password hundler")
# stackedWidget.addWidget(UI_Start())
# stackedWidget.addWidget(Ui_Reg())
# stackedWidget.addWidget(Ui_Log())
# stackedWidget.addWidget(ui_storage())
# while True:             
#     pager = open("main/local/page.txt", "r")
#     n = int(pager.read())
#     stackedWidget.setCurrentIndex(n)
#     stackedWidget.show()
#     sys.exit(app.exec_()) 