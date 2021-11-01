import sqlite3

class Load_Supply():
    def midi(self):
        base = sqlite3.connect("user.db")
        cur = base.cursor()
        midi = list()
        raw = cur.execute(f"SELECT * FROM userlist").fetchall()
        for i in range(len(raw)):
            midi.append(raw[i][1:4])
        return midi