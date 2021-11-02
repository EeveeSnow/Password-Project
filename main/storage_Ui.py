import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMainWindow
from supply.load_data_supply import Load_Supply as ld

class ui_storage(QWidget):
    def __init__(self):
        super().__init__()
        self.id = open("main/local/user.txt", "r").read()
        self.db = "main/local/hundler.db"
        uic.loadUi("main/design/storage.ui", self)
        self.setWindowTitle("Password hundler")
        self.con = sqlite3.connect("user.db")
        self.tableWidget.setColumnWidth(0, 663)
        for i in range(1, 3):
            self.tableWidget.setColumnWidth(i, 290)
        self.loadData()
        self.logButton.clicked.connect(self.log_out)

    def loadData(self):
        db = ld(self.db, self.id)
        hundle = db.midi()
        self.tableWidget.setRowCount(len(hundle))
        rownow = 0
        for column in hundle:
            for i in range(len(column)):
                self.tableWidget.setItem(rownow, i, QTableWidgetItem(str(column[i])))
            rownow += 1
    
    def log_out(self):
        open("main/local/user.txt", "w")
        sys.exit()