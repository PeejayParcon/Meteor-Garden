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
        
    def revealCount(self):
        if self.variables.Start:
            if self.variables.millisecs >= 999:
                self.variables.millisecs = 0

                if self.variables.seconds >= 59:
                    self.variables.seconds = 0

                    if self.variables.minutes >= 59:
                        self.helpers._resetEvent()
                        return
                    else:
                        self.variables.minutes += 1
                else:
                    self.variables.seconds += 1

            self.variables.millisecs += 1

        text = f"{'0' + str(self.variables.minutes) if self.variables.minutes < 10 else str(self.variables.minutes)} : {'0' + str(self.variables.seconds) if self.variables.seconds < 10 else str(self.variables.seconds)} : {('0' + str(self.variables.millisecs) if self.variables.millisecs < 10 else str(self.variables.millisecs))[0:2]}"
 
        self.variables.counterlabel.setText('<h2>' + text + '</h2>')