import sys
from PyQt5.QtWidgets import QApplication
from conversion import ConverterWindow

app = QApplication(sys.argv)
calculator = ConverterWindow()

sys.exit(app.exec_())