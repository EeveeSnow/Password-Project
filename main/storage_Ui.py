import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QTableWidgetItem, QApplication, QMainWindow

from supply.load_data_supply import Load_Supply as ld
from supply.adding_supply import AddSupply
from supply.enscryptor_supply import enscrype
from supply.search_supply import searcher
from supply.delete_supply import deletor

from design.adding import Add_Dialog as adding_ui
from design.search import Search_Dialog as search_ui
from design.delete import Ui_Dialog as delete_ui
class ui_storage(QWidget):
    def __init__(self):
        super().__init__()
        self.id = open("main/local/user.txt", "r").read()

        uic.loadUi("main/design/storage.ui", self)
        self.setWindowTitle("Password hundler")
        self.tableWidget.setColumnWidth(0, 663)
        for i in range(1, 3):
            self.tableWidget.setColumnWidth(i, 300)
        self.loadData()
        self.addButton.clicked.connect(self.add)
        self.logButton.clicked.connect(self.log_out)
        self.showButton.clicked.connect(self.show_pas)
        self.searchButton.clicked.connect(self.search)
        self.deleteButton.clicked.connect(self.deletion)

    def loadData(self):
        self.db = "main/local/hundler.db"
        db = ld(self.db, self.id)
        self.hundle = db.midi()
        print(self.hundle)
        self.tableWidget.setRowCount(len(self.hundle))
        rownow = 0
        for column in self.hundle:
            for i in range(len(column)):
                self.tableWidget.setItem(rownow, i, QTableWidgetItem(str(column[i])))
            rownow += 1
    
    def add(self):
        addup = ui_Add(self.id)
        if addup.exec():
            self.loadData()
        else:
            self.loadData()
        # popup = QMessageBox()
        # popup.
        # popup.setWindowTitle("Error")
        # popup.setText(error)
        # popup.exec_()
    def search(self):
        searcherup = ui_Search(self.id)
        searcherup.exec()

    def show_pas(self):
        db = enscrype(ld(self.db, self.id).midi(), self.id)
        hundle = db.crypto()
        print(hundle)
        i = 0
        for column in hundle:
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(column)))
            i += 1

    def log_out(self):
        open("main/local/user.txt", "w")
        sys.exit()
    
    def deletion(self):
        deleup = ui_Delete(self.id, self.hundle)
        if deleup.exec():
            self.loadData()
        else:
            self.loadData()


class ui_Add(QDialog, adding_ui):
    def __init__(self, idn):
        super().__init__()
        self.id = idn
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.okButton.clicked.connect(self.add)
        self.hideButton.clicked.connect(self.h)


    def add(self):
        site = self.siteEdit.text()
        mail = self.mailEdit.text()
        pas = self.passwordEdit.text()
        AddSupply(self.id, site, mail, pas).add()
        self.hide()
        
    
    def h(self):
        self.hide()


class ui_Search(QDialog, search_ui):
    def __init__(self, idn):
        super().__init__()
        self.id = idn
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.okButton.clicked.connect(self.search)
        self.hideButton.clicked.connect(self.h)

    def h(self):
        self.hide()
    
    def search(self):
        info = self.siteEdit.text()
        idn = self.comboBox.currentIndex()
        if idn == 2:
            hundler = searcher(self.id, idn, info).long()
        else:
            hundler = searcher(self.id, idn, info).fast()
        self.tableWidget.setRowCount(len(hundler))
        rownow = 0
        for column in hundler:
            for i in range(len(column)):
                self.tableWidget.setItem(rownow, i, QTableWidgetItem(str(column[i])))
            rownow += 1
        db = enscrype(hundler, self.id)
        hundle = db.crypto()
        print(hundle)
        i = 0
        for column in hundle:
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(column)))
            i += 1


class ui_Delete(QDialog, delete_ui):
    def __init__(self, idn, hundle):
        super().__init__()
        self.id = idn
        self.hundle = hundle
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.okButton.clicked.connect(self.dele)
        self.hideButton.clicked.connect(self.h)

    def h(self):
        self.hide()
    
    def dele(self):
        idr = self.siteEdit.text()
        deletor(self.id, self.hundle, idr).delet()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    self = QMainWindow()
    ui = UI_Start()
    ui.show()
    sys.exit(app.exec_())