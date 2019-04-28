# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import resources
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 700)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("*\n"
"{\n"
"    font :  11pt \"Verdana\";\n"
"    color : grey;\n"
"    border : 0px solid grey;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"    color : grey;\n"
"}\n"
"\n"
"QMainWindow\n"
"{\n"
"    background : #282828;\n"
"    min-width : 470px;\n"
"    max-height : 700px;\n"
"    max-width : 470px;\n"
"    min-height : 700px;\n"
"    opacity* : 100;\n"
"}\n"
"\n"
"QFrame#background\n"
"{\n"
"    background : #282828;\n"
"    opacity : 0;\n"
"}\n"
"\n"
"\n"
"QListWidget\n"
"{\n"
"    background : #333333;\n"
"    border-radius : 2px;\n"
"    border: 1px solid #444444;\n"
"    color : grey;\n"
"}\n"
"\n"
"QTextBrowser\n"
"{\n"
"    background : #1c1c1d;\n"
"    border-radius: 2px;\n"
"    border: 1px solid grey;\n"
"}\n"
"\n"
"QTextBrowser:hover\n"
"{\n"
"    background : #1c1c1d;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    font :  17pt \"Verdana\";\n"
"    color : white;\n"
"    background : #1c1c1d;\n"
"    border-radius: 2px;\n"
"    border: 1px solid grey;\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"\n"
"QLineEdit:hover\n"
"{\n"
"    background : #1c1c1d;\n"
"    border-radius: 2px;\n"
"    border: 1px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton\n"
"{\n"
"    color : grey;\n"
"    background : #1c1c1d;\n"
"    border-radius: 10px;\n"
"    border: 1px solid grey;\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{    \n"
"    color : #1c1c1d;\n"
"    background : white;\n"
"    border-radius: 10px;\n"
"    border: 1px solid #1c1c1d;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{    \n"
"    color : white;\n"
"    background : #1c1c1d;\n"
"    border-radius: 10px;\n"
"    border: 1px solid white;\n"
"}")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.background = QtWidgets.QFrame(self.centralWidget)
        self.background.setGeometry(QtCore.QRect(-1, -1, 471, 691))
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.frame = QtWidgets.QFrame(self.background)
        self.frame.setGeometry(QtCore.QRect(40, 100, 391, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 350, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 180, 350, 50))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 290, 350, 50))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 400, 350, 50))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 40, 60, 16))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(170, 150, 60, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(170, 260, 60, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(170, 370, 60, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.frame_2 = QtWidgets.QFrame(self.background)
        self.frame_2.setGeometry(QtCore.QRect(40, 590, 391, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(150, 20, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.background)
        self.label_5.setGeometry(QtCore.QRect(225, 60, 31, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/Logo/Element6.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 479, 19))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QConverter"))
        self.label.setText(_translate("MainWindow", "Decimal"))
        self.label_2.setText(_translate("MainWindow", "Binary"))
        self.label_3.setText(_translate("MainWindow", "Hex"))
        self.label_4.setText(_translate("MainWindow", "Octal"))
        self.pushButton.setText(_translate("MainWindow", "Convert"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

