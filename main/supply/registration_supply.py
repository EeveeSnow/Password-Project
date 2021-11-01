import sqlite3


class RegSupply():
    def __init__(self, nick, pas, key):
        self.n = nick
        self.p = pas
        self.m = key
    
    def cheack(self):
        if len(self.n) < 3:
            out = False
            reason = "Nickname too short"
        elif len(self.p) <= 8:
            out = False
            reason = "Password too short"
        elif len(self.p) > 32:
            out = False
            reason = "Password too long"
        elif len(self.n) > 16:
            out = False
            reason = "Nickname too long"
        else:
            out = True
            reason = None
        return out, reason
    
    def add(self):
        base = sqlite3.connect("user.db")
        cur = base.cursor()
        idn = int(cur.execute(f"SELECT * FROM userlist").fetchall()[-1][0]) + 1
        info = f'INSERT INTO userlist VALUES("{str(idn)}", "{self.n}", "{self.m}","{self.p}")'
        cur.execute(info)
        base.commit()

