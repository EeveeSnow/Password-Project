import sqlite3
import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from supply.load_data_supply import Load_Supply as ld

class ui_storage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main/design/Storage.ui", self)
        self.con = sqlite3.connect("user.db")
        self.tableWidget.setColumnWidth(0, 663)
        for i in range(1, 3):
            self.tableWidget.setColumnWidth(i, 300)
        self.loadData()

    def loadData(self):
        hundle = ld.midi(self)
        self.tableWidget.setRowCount(len(hundle))
        rownow = 0
        for column in hundle:
            for i in range(len(column)):
                self.tableWidget.setItem(rownow, i, QTableWidgetItem(str(column[i])))
            rownow += 1




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())