import sqlite3

class Load_Supply():
    def __init__(self, db, user):
        self.db = db
        self.user = user

    def midi(self):
        base = sqlite3.connect(self.db)
        cur = base.cursor()
        midi = list()
        try:
            raw = cur.execute(f"SELECT * FROM '{self.user}'").fetchall()
        except:
            raw = []
        for i in range(len(raw)):
            midi.append(raw[i])
        return midi