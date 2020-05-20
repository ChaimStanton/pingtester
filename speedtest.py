#! python3

from datetime import datetime
import logging
from time import sleep
import csv
import subprocess
import json

logging.basicConfig(filename='logfiles.log', filemode='a',
                    format='%(levelname)s:%(message)s:%(asctime)s', datefmt=r"%d/%m/%Y, %H:%M:%S",
                    level=logging.NOTSET)


def quotes(message):
    return "\'" + message + "\'"


class SpeedLog():
    def __init__(self, isConnected, output):
        self.isConnected = isConnected
        self.output = output

        self.time = timeSTR()
        self.text = self.time + " --- connected=" + str(self.isConnected) + " --- output: " + str(self.output)

        self.logToCSVtable()
        self.logToJSON()

    def logToCSVtable(self):
        with open("data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([str(self.isConnected), str(self.time), str(self.output)])

    def __dict__(self):
        return {
            "isConnected": self.isConnected,
            "time": self.time,
            "output": str(self.output)
        }

    def logToJSON(self):
        with open("data_output.json", "a") as writeFile:
            json.dump(self.__dict__(), writeFile, indent="\t")
            writeFile.write(",\n")


def timeSTR():
    a = datetime.now()
    return a.strftime(r"%d/%m/%Y, %H:%M:%S")


logging.debug("This is beginning of program")
with open("data_output.json", "a") as writeFile:
    writeFile.write("{")
try:
    while True:
        ping = subprocess.run("ping -c 1 8.8.8.8", stdout=subprocess.PIPE, shell=True)
        if ping.returncode == 0:
            pingPositive = True
        else:
            pingPositive = False

        SpeedLog(pingPositive, ping)
        sleep(1)
except KeyboardInterrupt:
    with open("data_output.json", "a") as writeFile:
        writeFile.write("\n}")
    logging.debug("End of program")
