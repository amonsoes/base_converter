from PyQt5 import QtWidgets
from base_converter import Ui_MainWindow

class ConverterWindow(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()