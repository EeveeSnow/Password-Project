import time
from PyQt5.QtCore import QThread


class updater(QThread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        pager = open("local/page.txt", "r")
        n = int(pager.read())
        pager.close()
        time.sleep(0.5)
        return(n)

    