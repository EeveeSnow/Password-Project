import sqlite3


class to_txt():
    def __init__(self, idn, hundle, pas):
        self.id = idn
        self.hundle = hundle
        self.pas = pas
        self.txt = "main/local/page.txt"

    def convert(self):
        text = open(self.txt, "w")
        for i in range(len(self.hundle)):
            text.write("_" * 100 + "\n")
            text.write(f"|      site:     |{self.hundle[i][0]:^81}|\n".format(self.hundle[i]))
            text.write("_" * 100 + "\n")
            text.write(f"|      mail:     |{self.hundle[i][1]:^81}|\n".format(self.hundle[i]))
            text.write("_" * 100 + "\n")
            text.write(f"|      pas:      |{self.pas[i]:^81}|\n".format(self.pas))
        text.close()

