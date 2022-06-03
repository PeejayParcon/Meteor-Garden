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
        
    def uiComponents(self):
        self.variables.counterlabel.setFixedSize(int(self.variables.window_width * 0.75), int(self.variables.window_height * 0.10))
        self.variables.counterlabel.move(int(self.rect().width() / 2 - self.variables.counterlabel.rect().width() / 2), int(self.variables.window_height * 0.13))

        if self.variables.screen_rect.width() == 1024 and self.variables.screen_rect.height() == 768:
            self.variables.counterlabel.setFont(QFont('Courier', 15, QFont.Bold))
        else:
            self.variables.counterlabel.setFont(QFont('Courier', 20, QFont.Bold))

        self.variables.counterlabel.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Start button
        self.variables.startbutton.setFixedSize(self.variables.buttonwidth, self.variables.buttonheight)
        self.variables.startbutton.move(int(self.variables.window_width * 0.17), int(self.variables.counterlabel.y() + self.variables.counterlabel.height() + (self.variables.window_height * 0.05)))
        self.variables.startbutton.pressed.connect(self.helpers.startEv)

        # Stop button
        self.variables.stopbutton.setFixedSize(self.variables.buttonwidth, self.variables.buttonheight)
        self.variables.stopbutton.move(int(self.variables.buttonwidth + self.variables.startbutton.x() + self.variables.window_width * 0.02), int(self.variables.counterlabel.y() + self.variables.counterlabel.height() + (self.variables.window_height * 0.05)))
        self.variables.stopbutton.pressed.connect(self.helpers.stopEv)