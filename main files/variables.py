from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QLabel

class Variables():
    def __init__(self, main):
        self.screen_rect = QApplication.desktop().screen().rect()
        self.window_width = int(self.screen_rect.width() * 0.30)
        self.window_height = int(self.screen_rect.height() * 0.50)

        self.Start = False

        self.seconds = 0
        self.minutes = 0
        self.millisecs = 0
        
        self.column = 0
        self.prev_seconds = 0
        self.prev_minutes = 0
        self.prev_millisecs = 0

        self.buttonwidth = int(self.window_width * 0.15)
        self.buttonheight = int(self.window_height * 0.07)

        self.counterlabel = QLabel(main)
        self.startbutton = QPushButton("START", main)
        self.stopbutton = QPushButton("STOP", main)
        self.resetbutton = QPushButton("RESET", main)
        self.splitbutton = QPushButton("SPLIT (Lap)", main)
        self.datatable = QTableWidget(main)
