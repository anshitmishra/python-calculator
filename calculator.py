from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 506)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setWindowIcon(QtGui.QIcon('image/calculator.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.InputBox = QtWidgets.QLineEdit(self.centralwidget)
        self.InputBox.setGeometry(QtCore.QRect(10, 10, 311, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.InputBox.setFont(font)
        self.InputBox.setText("")
        self.InputBox.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.InputBox.setReadOnly(True)
        self.InputBox.setClearButtonEnabled(False)
        self.InputBox.setObjectName("InputBox")
        self.button_1 = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("1"))
        self.button_1.setGeometry(QtCore.QRect(10, 110, 71, 71))
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("2"))
        self.button_2.setGeometry(QtCore.QRect(90, 110, 71, 71))
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("3"))
        self.button_3.setGeometry(QtCore.QRect(170, 110, 71, 71))
        self.button_3.setObjectName("button_3")
        self.button_Plus = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("+"))
        self.button_Plus.setGeometry(QtCore.QRect(250, 110, 71, 71))
        self.button_Plus.setObjectName("button_Plus")
        self.button_8 = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("8"))
        self.button_8.setGeometry(QtCore.QRect(90, 290, 71, 71))
        self.button_8.setObjectName("button_8")
        self.button_9 = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("9"))
        self.button_9.setGeometry(QtCore.QRect(170, 290, 71, 71))
        self.button_9.setObjectName("button_9")
        self.button_Multiply = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("*"))
        self.button_Multiply.setGeometry(QtCore.QRect(250, 290, 71, 71))
        self.button_Multiply.setObjectName("button_Multiply")
        self.button_7 = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("7"))
        self.button_7.setGeometry(QtCore.QRect(10, 290, 71, 71))
        self.button_7.setObjectName("button_7")
        self.button_Minus = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("-"))
        self.button_Minus.setGeometry(QtCore.QRect(250, 200, 71, 71))
        self.button_Minus.setObjectName("button_Minus")
        self.button_5 = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("5"))
        self.button_5.setGeometry(QtCore.QRect(90, 200, 71, 71))
        self.button_5.setObjectName("button_5")
        self.button_6 = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("6"))
        self.button_6.setGeometry(QtCore.QRect(170, 200, 71, 71))
        self.button_6.setObjectName("button_6")
        self.button_4 = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("4"))
        self.button_4.setGeometry(QtCore.QRect(10, 200, 71, 71))
        self.button_4.setObjectName("button_4")
        self.button_divide = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("/"))
        self.button_divide.setGeometry(QtCore.QRect(250, 380, 71, 71))
        self.button_divide.setObjectName("button_divide")
        self.button_Equal = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("="))
        self.button_Equal.setGeometry(QtCore.QRect(170, 380, 71, 71))
        self.button_Equal.setObjectName("button_Equal")
        self.button_clear = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("X"))
        self.button_clear.setGeometry(QtCore.QRect(10, 380, 71, 71))
        self.button_clear.setObjectName("button_clear")
        self.button_0 = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.press_it("0"))
        self.button_0.setGeometry(QtCore.QRect(90, 380, 71, 71))
        self.button_0.setObjectName("button_0")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.InputBox.setText(_translate("MainWindow", "0"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_Plus.setText(_translate("MainWindow", "+"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_Multiply.setText(_translate("MainWindow", "*"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_Minus.setText(_translate("MainWindow", "-"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_divide.setText(_translate("MainWindow", "/"))
        self.button_Equal.setText(_translate("MainWindow", "="))
        self.button_clear.setText(_translate("MainWindow", "X"))
        self.button_0.setText(_translate("MainWindow", "0"))

    def press_it(self, key):
        if key == "X":
            sceen = self.InputBox.text()
            sceen = sceen[:-1]
            self.InputBox.setText(sceen)
        elif key == "=":
            sceen = self.InputBox.text()
            try:
                total = round(eval(sceen), 5)

                self.InputBox.setText(f'{total}')
            except:
                self.InputBox.setText("error")
        else:
            if self.InputBox.text() == "0":
                self.InputBox.setText("")
            if self.InputBox.text() == "error":
                self.InputBox.setText("")
            self.InputBox.setText(f'{self.InputBox.text()}{key}')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
