import sqlite3

class deletor():
    def __init__(self, idn, hundle, idr):
        self.id = idn
        self.hundle = hundle[int(idr) - 1]
    
    def delet(self):
        self.db = "main/local/hundler.db"
        base = sqlite3.connect(self.db)
        cur = base.cursor()
        d = f"DELETE FROM '{self.id}' WHERE site='{self.hundle[0]}' AND login='{self.hundle[1]}' AND password='{self.hundle[2]}' AND date='{self.hundle[3]}'"
        cur.execute(d)
        base.commit()