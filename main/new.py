from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_New(object):
    def setupUi(self, New):
        New.setObjectName("New")
        New.resize(500, 600)
        self.centralwidget = QtWidgets.QWidget(New)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 200, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 270, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        New.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(New)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        New.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(New)
        self.statusbar.setObjectName("statusbar")
        New.setStatusBar(self.statusbar)

        self.retranslateUi(New)
        QtCore.QMetaObject.connectSlotsByName(New)

    def retranslateUi(self, New):
        _translate = QtCore.QCoreApplication.translate
        New.setWindowTitle(_translate("New", "New"))
        self.pushButton_3.setText(_translate("New", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New = QtWidgets.QMainWindow()
    ui = Ui_New()
    ui.setupUi(New)
    New.show()
    sys.exit(app.exec_())
