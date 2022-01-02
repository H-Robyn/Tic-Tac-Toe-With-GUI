import sys
from PyQt6.QtWidgets import QApplication, QDialog
from TTT import *


class GameRunner(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.setCenteralWidget(self)
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = GameRunner()
    w.show()
    sys.exit(app.exec())
