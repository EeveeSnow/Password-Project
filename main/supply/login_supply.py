import sqlite3


class LogSupply():
    def __init__(self, nick, pas):
        self.n = nick
        self.p = pas
    
    def cheack(self):
        base = sqlite3.connect("local/user.db")
        cur1 = base.cursor()
        cur2 = base.cursor()
        cur = base.cursor()
        if cur1.execute(f"SELECT * FROM userlist WHERE nickname = '{self.n}'").fetchall() == cur2.execute(f"SELECT * FROM userlist WHERE password = '{self.p}'").fetchall() and cur1.execute(f"SELECT * FROM userlist WHERE nickname = '{self.n}'").fetchall() != []:
            return cur.execute(f"SELECT * FROM userlist WHERE nickname = '{self.n}'").fetchall()[0][0]
        else:
            return -1