#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt

import sys

from methods import FundaMethods
from variables import Variables

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stopwatch")

        self.variables = Variables(self)

        self.setFixedSize(self.variables.window_width, self.variables.window_height)
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())

        self.helpers = FundaMethods(self.variables)

        timer = QTimer(self)
        timer.timeout.connect(self.revealCount)
        timer.start(1)

        self.uiComponents()