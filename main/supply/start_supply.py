import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
)

class UI_Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
    
    def setupUI(self):
        self.setObjectName("Main")
        self.setWindowTitle("Password hundler")
        self.resize(1280, 720)
        layout = QVBoxLayout()
        self.setLayout(layout)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     Main = QtWidgets.QMainWindow()
#     ui = UI_Main()
#     ui.setupUI(Main)
#     Main.Show()
#     sys.exit(app.exec_())