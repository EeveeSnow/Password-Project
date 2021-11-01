import sqlite3

from PyQt5.uic import compileUiDir
base = sqlite3.connect("user.db")
cur = base.cursor()
midi = list()
raw = cur.execute(f"SELECT * FROM userlist").fetchall()
for i in range(len(raw)):
    midi.append(raw[i][1:4])
print(midi)