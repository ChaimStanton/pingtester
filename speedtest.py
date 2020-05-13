#! python3

import urllib.request
from datetime import datetime
import logging
from time import sleep
import csv
from os import system


logging.basicConfig(filename='speedtest.log', filemode='a',
                    format='%(message)s')

severityMessgDICT = {1: "info",
                     2: "good",
                     3: "BAD",
                     4: "medium"}


def quotes(message):
    return "\'" + message + "\'"


class log():
    def __init__(self, message, severity):
        self.message = message
        self.severity = severity

        self.time = timeSTR()
        self.severityMSG = severityMessgDICT[severity]
        self.text = "---" + self.severityMSG + "--- " + "at --- " + self.time + " --- " + self.message

        self.logLogFile()
        # self.logHTML()
        self.logToCSVtable()

    # def logHTML(self):
    #     with open("index.html", "a") as htmlFile:
    #         htmlFile.write(self.text + "<br>")

    def logToCSVtable(self):
        with open("data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([self.severityMSG, self.message, self.time])

    def logLogFile(self):
        logging.warning(self.text)


def timeSTR():
    a = datetime.now()
    return a.strftime(r"%d/%m/%Y, %H:%M:%S")


def am_I_connected(time):
    try:
        urllib.request.urlopen("http://google.com", timeout=time)
        return True
    except urllib.error.URLError:
        return False

# while True:
#     if am_I_connected(3) == True:
#         log("Connected to internet", 2)
#     elif am_I_connected(10) == True:
#         log("timed out after 3 seconds but not after 10", 4)
#     else:
#         log("Not connected to internet timed out after 10 seconds", 3)
#     sleep(300)


log("This is beginning of program format of date is day/month/year, hour, minute, second \n This is v0.2.1", 1)

while True:
    system("nohup speedtest-cli > speedTestResults.out")
    with open("speedTestResults.out", "r") as textFile:
        speedTestTEXT = textFile.read()
        print(speedTestTEXT)
        log(speedTestTEXT, 1)
    print("sleeping")
    sleep(300)


log("end of program", 1)
