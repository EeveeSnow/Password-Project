#<--*-- coding:utf-8 --*-->
from PyQt5.QtWidgets import QMainWindow, QApplication
from main import Ui_Main
from show import Ui_Show
from new import Ui_New
import sys
 
class Main(QMainWindow,Ui_Main):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.child1 = Show()
        self.child2 = New()
        self.action_2.triggered.connect(self.New)
        self.action.triggered.connect(self.Show)
    def Show(self):
        self.gridLayout.addWidget (self.child1) # Помещаем окно в gridLayout
        self.child1.show () # Открыть дочернее окно 1
    def New(self):
        self.gridLayout_2.addWidget(self.child2)
        self.child2.show()
 
class New(QMainWindow,Ui_New):
    def __init__(self):
        super(New,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Close)
    def Close(self):
        self.close()
 
class Show(QMainWindow,Ui_Show):
    def __init__(self):
        super(Show,self).__init__()
        self.setupUi(self)
 
if __name__=='__main__':
    app = QApplication(sys.argv)
    Main = Main()
    Show = Show()
    New = New()
    Main.show()
    sys.exit(app.exec_())