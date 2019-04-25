from PyQt5 import QtWidgets
from base_converter import Ui_MainWindow


class ConverterWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.show()
        self.line_list = []

        self.line_list.append(self.lineEdit)
        self.line_list.append(self.lineEdit_2)
        self.line_list.append(self.lineEdit_3)
        self.line_list.append(self.lineEdit_4)

        self.pushButton.clicked.connect(self.do_conversion)

    # lineEdit = decimal
    # lineEdit_2 = binary
    # lineEdit_3 = hex
    # lineEdit_4 = octal

    def do_conversion(self):
        for line_edit in self.line_list:
            if line_edit.text() != "":
                print(line_edit.objectName(), line_edit.text())
                for other in self.line_list:

                    # convert from decimal
                    if line_edit.objectName() == "lineEdit":

                        for digit in line_edit.text():
                            if digit not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                                line_edit.setText("INVALID ENTRY")
                                return None

                        if other.objectName() == "lineEdit":
                            other.setText(line_edit.text())
                        elif other.objectName() == "lineEdit_2":
                            other.setText(str(bin(int(line_edit.text())))[2:])
                        elif other.objectName() == "lineEdit_3":
                            other.setText(str(hex(int(line_edit.text())))[2:].upper())
                        elif other.objectName() == "lineEdit_4":
                            other.setText(str(oct(int(line_edit.text())))[2:])

                    # convert from binary
                    if line_edit.objectName() == "lineEdit_2":

                        for digit in line_edit.text():
                            if digit not in ["0", "1"]:
                                line_edit.setText("INVALID ENTRY")
                                return None

                        if other.objectName() == "lineEdit":
                            other.setText(str(int(line_edit.text(), 2)))
                        elif other.objectName() == "lineEdit_2":
                            other.setText(line_edit.text())
                        elif other.objectName() == "lineEdit_3":
                            other.setText(str(hex(int(line_edit.text(), 2)))[2:].upper())
                        elif other.objectName() == "lineEdit_4":
                            other.setText(str(oct(int(line_edit.text(), 2)))[2:])

                    # convert from hex
                    if line_edit.objectName() == "lineEdit_3":

                        if other.objectName() == "lineEdit":
                            other.setText(str(int(line_edit.text(), 16)))
                        elif other.objectName() == "lineEdit_2":
                            other.setText(str(bin(int(line_edit.text(), 16)))[2:])
                        elif other.objectName() == "lineEdit_3":
                            other.setText(line_edit.text())
                        elif other.objectName() == "lineEdit_4":
                            other.setText(str(oct(int(line_edit.text(), 16)))[2:])

                    # convert from octal
                    if line_edit.objectName() == "lineEdit_4":

                        for digit in line_edit.text():
                            if digit not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
                                line_edit.setText("INVALID ENTRY")
                                return None

                        if other.objectName() == "lineEdit":
                            other.setText(str(int(line_edit.text(), 8)))
                        elif other.objectName() == "lineEdit_2":
                            other.setText(str(bin(int(line_edit.text(), 8)))[2:])
                        elif other.objectName() == "lineEdit_3":
                            other.setText(str(hex(int(line_edit.text(), 8)))[2:].upper())
                        elif other.objectName() == "lineEdit_4":
                            other.setText(line_edit.text())

    def analyze_input(self):
        pass



