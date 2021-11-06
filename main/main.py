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
        # QWidget.statusBar(self).setVisible(False)
        idn = open("main/local/user.txt", "r").read()
        if idn == "":
            self.start = UI_Start()
            self.start.show()    
        else: 
            self.storage = ui_storage()
            self.storage.show()
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    hundler = Hundler()
    sys.exit(app.exec_())