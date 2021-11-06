import sqlite3
import datetime as dt
import random as rd

class AddSupply():
    def __init__(self, idn, site, mail, password):
        self.id = idn
        self.site = site
        self.mail = mail
        self.pas = password
        self.date = str(dt.date.today()).split("-")
        self.db = "local/hundler.db"
        self.db2 = "local/user.db"

    def add(self):
        base = sqlite3.connect(self.db)
        cur = base.cursor()
        base2 = sqlite3.connect(self.db2)
        cur2 = base2.cursor()
        self.key = str(cur2.execute(f"SELECT * FROM userlist WHERE id = '{self.id}'").fetchall()[0][2] + 1234000)
        self.pas = self.crypt()
        self.date = "-".join(self.date)
        info = f'INSERT INTO "{self.id}" VALUES("{str(self.site)}", "{self.mail}", "{self.pas}","{self.date}")'
        cur.execute(info)
        base.commit()

    def crypt(self):
        newpas = list()
        for i in self.pas:
            newi = chr(ord(i) + int(self.key[int(self.date[0][2])]) + int(self.key[int(self.date[1][0])]))
            newpas.append(newi)
        for c in range(0, len(self.pas), int(self.date[2][1])):
            newpas.insert(c, chr(rd.randint(1, 255)))
        return "".join(newpas)


