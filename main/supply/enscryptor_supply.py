import sqlite3
import numpy as np


class enscrype():
    def __init__(self, hundler, idn):
        self.db2 = "main/local/user.db"
        self.id = idn
        self.hundler = hundler
        base = sqlite3.connect(self.db2)
        cur = base.cursor()
        self.key = str(cur.execute(f"SELECT * FROM userlist WHERE id = '{self.id}'").fetchall()[0][2] + 1234000)

    def crypto(self):
        pas = list()
        for look in self.hundler:
            pasnow = list()
            newl = ""
            pasnow.extend(look[2])
            datenow = str(look[3]).split("-")
            wrong = pasnow[:len(pasnow) - len(pasnow) // int(datenow[2][1]):int(datenow[2][1])]
            pasnow = list(np.setdiff1d(pasnow, wrong, assume_unique = True))
            for letter in pasnow:
                newl += chr(ord(letter) - int(self.key[int(datenow[0][2])]) - int(self.key[int(datenow[1][0])]))
            pas.append(newl)
        return pas

