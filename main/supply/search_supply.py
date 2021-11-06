import sqlite3
from supply.enscryptor_supply import enscrype


class searcher():
    def __init__(self, idn, type, info):
        self.db = "local/hundler.db"
        self.id = idn
        self.info = info
        self.type = ["site", "login", "password"][type]
    
    def fast(self):
        base = sqlite3.connect(self.db)
        cur = base.cursor()
        data = cur.execute(f"SELECT * FROM '{self.id}' WHERE {self.type} = '{self.info}'").fetchall()
        return data

    def long(self):
        out = list()
        base = sqlite3.connect(self.db)
        cur = base.cursor()
        data = cur.execute(f"SELECT * FROM '{self.id}'").fetchall()
        pas = enscrype(data, self.id).crypto()
        for i in range(len(pas)):
            if pas[i] == self.info:
                out.append(data[i])
        return out