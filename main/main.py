import sys

from PyQt5.QtWidgets import QApplication, QWidget

from start_Ui import UI_Start
from storage_Ui import ui_storage


class Hundler(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password hundler")
        # QWidget.statusBar(self).setVisible(False)
        idn = open("local/user.txt", "r").read()
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
