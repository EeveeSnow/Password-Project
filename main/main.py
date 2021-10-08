import sys
import sqlite3

#типо импорт для интерфейса
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLineEdit, QLCDNumber,QLabel
from PyQt5.QtCore import QRect, Qt

now_id = None
class Ui_Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QRect(230, 120, 631, 371))

    def initUI(self) -> None:
        pass


class RegistrationOrLogin(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)
    
    def initUI(self, args):
        self.btn = QPushButton('Другая форма', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 100)


class Registration(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)
    
    def initUI(self, args):
        self.setGeometry(QRect(0, 0, 631, 371))
        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setGeometry(QRect(230, 280, 171, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QRect(232, 220, 161, 31))
        self.lineEdit.setInputMethodHints(Qt.ImhHiddenText)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QRect(230, 170, 161, 31))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Main()
    ex.show()
    sys.exit(app.exec())