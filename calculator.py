# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 492, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"border: 2px solid rgb(255,255,255);")
        self.label_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_result.setObjectName("label_result")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 432, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_0.setObjectName("btn_0")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(294, 304, 100, 258))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_add.setObjectName("btn_add")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 304, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(98, 304, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(196, 304, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_9.setObjectName("btn_9")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 176, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(98, 176, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(196, 176, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_6.setObjectName("btn_6")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 48, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(98, 48, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(196, 48, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_3.setObjectName("btn_3")
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(98, 432, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dot.setFont(font)
        self.btn_dot.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_dot.setObjectName("btn_dot")
        self.btn_radical = QtWidgets.QPushButton(self.centralwidget)
        self.btn_radical.setGeometry(QtCore.QRect(196, 432, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_radical.setFont(font)
        self.btn_radical.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_radical.setObjectName("btn_radical")
        self.btn_result = QtWidgets.QPushButton(self.centralwidget)
        self.btn_result.setGeometry(QtCore.QRect(392, 304, 100, 258))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_result.setFont(font)
        self.btn_result.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_result.setObjectName("btn_result")
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setGeometry(QtCore.QRect(294, 48, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_div.setFont(font)
        self.btn_div.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_div.setObjectName("btn_div")
        self.btn_mult = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mult.setGeometry(QtCore.QRect(294, 176, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mult.setFont(font)
        self.btn_mult.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_mult.setObjectName("btn_mult")
        self.btn_perc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_perc.setGeometry(QtCore.QRect(392, 48, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_perc.setFont(font)
        self.btn_perc.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_perc.setObjectName("btn_perc")
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sub.setGeometry(QtCore.QRect(392, 176, 100, 130))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_sub.setFont(font)
        self.btn_sub.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(255,255,255);")
        self.btn_sub.setObjectName("btn_sub")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 492, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuTheme = QtWidgets.QMenu(self.menuBar)
        self.menuTheme.setObjectName("menuTheme")
        MainWindow.setMenuBar(self.menuBar)
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setObjectName("actionLight")
        self.actionIPhone = QtWidgets.QAction(MainWindow)
        self.actionIPhone.setObjectName("actionIPhone")
        self.menuTheme.addSeparator()
        self.menuTheme.addAction(self.actionDark)
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addAction(self.actionIPhone)
        self.menuBar.addAction(self.menuTheme.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_radical.setText(_translate("MainWindow", "√"))
        self.btn_result.setText(_translate("MainWindow", "="))
        self.btn_div.setText(_translate("MainWindow", "÷"))
        self.btn_mult.setText(_translate("MainWindow", "×"))
        self.btn_perc.setText(_translate("MainWindow", "%"))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.menuTheme.setTitle(_translate("MainWindow", "Theme"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionIPhone.setText(_translate("MainWindow", "IPhone"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
