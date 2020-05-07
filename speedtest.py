#! python3

import urllib.request
from datetime import datetime
import logging
from time import sleep

logging.basicConfig(filename='speedtest.log', filemode='a', format='%(message)s')

severityMessgDICT = {1 : "info",
                     2 : "good",
                     3 : "BAD",
                     4 : "meduim"}

def log(message, severity):
    # 1 for informational 2 for good 3 for bad
    text = "---" + severityMessgDICT[severity] + "--- " + "at --- " + timeSTR() + " --- " + message
    with open("index.html", "a") as htmlFile:
        htmlFile.write(text + "<br>")
    logging.warning(text)

def timeSTR():
    a = datetime.now()
    return a.strftime(r"%d/%m/%Y, %H:%M:%S")

def am_I_connected(time):
    try:
        urllib.request.urlopen("http://google.com", timeout=time)
        return True
    except urllib.error.URLError:
        return False

log("This is beginning of program format of date is day/month/year, hour, minute, second",1)

while True:
    if am_I_connected(3) == True:
        log("Connected to internet", 2)
    elif am_I_connected(10) == True:
        log("timed out after 3 seconds but not after 10", 4)
    else:
        log("Not connected to internet timed out after 10 seconds", 3)
    sleep(300)

log("end of program", 1)
