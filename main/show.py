# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Show(object):
    def setupUi(self, Show):
        Show.setObjectName("Show")
        Show.resize(500, 600)
        self.centralwidget = QtWidgets.QWidget(Show)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 200, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 270, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        Show.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Show)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        Show.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Show)
        self.statusbar.setObjectName("statusbar")
        Show.setStatusBar(self.statusbar)

        self.retranslateUi(Show)
        QtCore.QMetaObject.connectSlotsByName(Show)

    def retranslateUi(self, Show):
        _translate = QtCore.QCoreApplication.translate
        Show.setWindowTitle(_translate("Show", "Show"))
        self.pushButton_3.setText(_translate("Show", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Show = QtWidgets.QMainWindow()
    ui = Ui_Show()
    ui.setupUi(Show)
    Show.show()
    sys.exit(app.exec_())