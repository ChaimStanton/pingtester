#! python3

import urllib.request
from datetime import datetime
import logging
from time import sleep, strftime
import csv
from os import system
import subprocess

logging.basicConfig(filename='logfiles.log', filemode='a',
                    format='%(levelname)s:%(message)s:%(asctime)s', datefmt=r"%d/%m/%Y, %H:%M:%S",
                    level=logging.NOTSET)

severityMessgDICT = {1: "info",
                     2: "good",
                     3: "BAD "}


def quotes(message):
    return "\'" + message + "\'"

class SpeedLog():
    def __init__(self, message, severity, isConnected=None, output=None):
        self.message = message
        self.severity = severity
        self.isConnected = isConnected
        self.output=output

        self.time = timeSTR()
        self.severityMSG = severityMessgDICT[severity]
        self.text = "---" + self.severityMSG + "--- " + "at --- " + self.time + " --- connected=" + str(self.isConnected) + " --- output: " + str(self.output)

        self.logLogFile()
        # self.logHTML()
        self.logToCSVtable()

    def logToCSVtable(self):
        with open("data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([self.severityMSG, self.message, self.time])

    def logLogFile(self):
        logging.warning(self.text)


def timeSTR():
    a = datetime.now()
    return a.strftime(r"%d/%m/%Y, %H:%M:%S")

logging.info("This is beginning of program")

while True:
    ping = subprocess.run("ping -c 1 8.8.8.8", stdout=subprocess.PIPE, shell=True)
    if ping.returncode == 0:
        pingPositive = True
        severityMessg = 2 # good
        message = "Connected"
    else:
        pingPositive = False
        severityMessgDICT = 3 # bad
        message = "Not connected"

logging.info("End of program")
