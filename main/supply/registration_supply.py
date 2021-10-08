import sqlite3
from db_supply import database_list
class RegSupply():
    def __init__(self, nick, pas):
        self.n = nick
        self.p = pas
    
    def cheack(self):
        if len(self.n) < 3:
            out = False
            reason = "Nickname too short"
        elif len(self.p) < 8:
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
        base = sqlite3.connect(database_list.db_list[1])
        cur = base.cursor()
        cur.execute("INSERT INTO userlist VALUE(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        ("0000000000000001", self.n, self.p, "0000", "False", "False", "False", "False", "False", "None"))
        base.commit()

RegSupply("popipo", "005")

