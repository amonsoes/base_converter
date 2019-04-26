from PyQt5 import QtWidgets, QtCore
from base_converter import Ui_MainWindow


class ConverterWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    resized = QtCore.pyqtSignal()

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.show()
        self.line_list = []
        self.event_list = []

        self.line_list.append(self.lineEdit)
        self.line_list.append(self.lineEdit_2)
        self.line_list.append(self.lineEdit_3)
        self.line_list.append(self.lineEdit_4)

        self.pushButton.clicked.connect(self.do_conversion)

        self.lineEdit.textEdited.connect(lambda x: self.event_list.append((self.lineEdit.objectName(), x)))
        self.lineEdit_2.textEdited.connect(lambda x: self.event_list.append((self.lineEdit_2.objectName(), x)))
        self.lineEdit_3.textEdited.connect(lambda x: self.event_list.append((self.lineEdit_3.objectName(), x)))
        self.lineEdit_4.textEdited.connect(lambda x: self.event_list.append((self.lineEdit_4.objectName(), x)))
        self.resized.connect(self.resized_function)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(ConverterWindow, self).resizeEvent(event)

    def resized_function(self):
        print(self.centralWidget().objectName())

    # lineEdit = decimal
    # lineEdit_2 = binary
    # lineEdit_3 = hex
    # lineEdit_4 = octal

    def do_conversion(self):

        # clean up space in event list
        if len(self.event_list) > 10:
            self.event_list = self.event_list[-10:]

        # go through the line edits to find the one with the edited text
        for line_edit in self.line_list:
            if line_edit.objectName() == self.event_list[-1][0]:
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

                        for digit in line_edit.text():
                            if digit not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a",
                                             "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]:
                                line_edit.setText("INVALID ENTRY")
                                return None

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
