import sqlite3


class MasterSupply():
    def __init__(self, master):
        self.m = master

    def cheack(self):
        def isint(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        if len(self.m) < 2:
            out = False
            reason = "Key too short"
        elif len(self.m) > 8:
            out = False
            reason = "Key too long"
        else:
            out = isint(self.m)
            reason = "Key can be only integer"
        return out, reason