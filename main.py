import os
from pathlib import Path
import sys
import time

from PasswordGen import Generator

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi

class MainWindow(QMainWindow):
        def __init__(self):
                super(MainWindow, self).__init__()
                self._displayedit = QLineEdit
                self._displaypass = QLabel
                loadUi("form.ui", self)

                self._genpass.clicked.connect(self._genpassClicked)

        def _genpassClicked(self):
                if (self._displayedit.text()).isdigit() == True:
                        pwd = Generator(int(self._displayedit.text()))
                        self._displaypass.setText(f"Password: {pwd}")
                        text = self._displaypass.text()
                        text=text[9:]
                        clipboard = QApplication.clipboard()
                        clipboard.setText(text)
                        #time.sleep(1)
                else:
                        self._displaypass.setText("Password: Not digit.")
                        self._displaypass.clear()
if __name__ == "__main__":
        
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec())