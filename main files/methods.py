from PyQt5.QtWidgets import QTableWidgetItem
from datetime import timedelta

class FundaMethods():
    def __init__(self, variables):
        self.variables = variables

    def startEv(self):
        self.variables.Start = True

    def stopEv(self):
        self.variables.Start = False

    def resetEv(self):
        self.variables.Start = False
        self.variables.seconds = 0
        self.variables.minutes = 0
        self.variables.millisecs = 0
        self.variables.column = 0

        self.variables.datatable.clearContents()

        self.variables.counterlabel.setText("00m : 00s . 00")
        self.variables.startbutton.setText("START")


    def splitEv(self):
        if self.variables.Start:
            minutes = '0' + str(self.variables.minutes) if self.variables.minutes < 10 else str(self.variables.minutes)
            seconds = '0' + str(self.variables.seconds) if self.variables.seconds < 10 else str(self.variables.seconds)
            millisecs = '0' + str(self.variables.millisecs) if self.variables.millisecs < 10 else str(self.variables.millisecs)
    
            text = f"{minutes} : {seconds} : {millisecs[0:2]}"
 
            self.variables.datatable.setItem(self.variables.column, 0, QTableWidgetItem(str(self.variables.column+ 1)))
            self.variables.datatable.setItem(self.variables.column, 1, QTableWidgetItem(f"{text}"))

            if self.variables.column == 0:
                self.variables.datatable.setItem(self.variables.column, 2, QTableWidgetItem(f"{text}"))
            else:
                time_length = str(timedelta(minutes=int(self.variables.minutes), seconds=int(self.variables.seconds), milliseconds=int(self.variables.millisecs)) - timedelta(minutes=int(self.variables.prev_minutes), seconds=int(self.variables.prev_seconds), milliseconds=int(self.variables.prev_millisecs)))
                final_result = f"{time_length[2:4]} : {time_length[5:7]} : {time_length[8:10]}"
                self.variables.datatable.setItem(self.variables.column, 2, QTableWidgetItem(f"{final_result}"))

            self.variables.column+= 1

        self.variables.prev_minutes = self.variables.minutes
        self.variables.prev_seconds = self.variables.seconds
        self.variables.prev_millisecs = self.variables.millisecs
