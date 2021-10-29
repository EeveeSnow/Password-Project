import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication
from start_Ui import UI_Start as start
from registration_Ui import Ui_Reg as reg
from loggin_Ui import Ui_Log as log
from supply.start_supply import UI_Main as main
import sys

class Main(QMainWindow,main):
    def __init__(self):
        super(Main,self).__init__()
        self.setupUi(self)
        self.show()
        self.reg = Reg()
        self.log = Log()
        self.action_2.triggered.connect(self.New)
        self.action.triggered.connect(self.Show)
    def Show(self):
        self.gridLayout.addWidget (self.reg) #Помещаем окно в gridLayout
        self.reg.show() #Открыть дочернее окно 1
    def New(self):
        self.gridLayout_2.addWidget(self.log)
        self.log.show()
        
 
class Log(QMainWindow, log):
    def __init__(self):
        super(Log,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Close)
    def Close(self):
        self.close()
 
class Reg(QMainWindow,reg):
    def __init__(self):
        super(Reg,self).__init__()
        self.setupUi(self)
 
if __name__=='__main__':
    app = QApplication(sys.argv)
    Main.show()
    sys.exit(app.exec_())