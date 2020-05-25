#! python3

from datetime import datetime
import logging
from time import sleep
import csv
import subprocess
import json

DATA_OUTPUT_CSV_FILE_NAME = "data.csv"

def CSVtooBig(csvFile):
    with open(csvFile, 'w+') as csvFile:
        reader = csv.reader(csvFile)
        lines = list(reader)

        linesToKeep = lines[-86400:-1] # the values from the last 24 hours
        writer = csv.writer(csvFile)
        writer.writerows(linesToKeep)

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
        with open(DATA_OUTPUT_CSV_FILE_NAME, "a") as file:
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

if __name__ == "__main__":
    try:
        logging.debug("This is beginning of program")
        with open("data_output.json", "a") as writeFile:
            writeFile.write("{")
            while True:
                linesWritten = 0
                while linesWritten <= 3600: # seeing as it writes a line every hour this would be a after 1 hour
                    ping = subprocess.run("ping -c 1 8.8.8.8", stdout=subprocess.PIPE, shell=True)
                    if ping.returncode == 0:
                        pingPositive = True
                    else:
                        pingPositive = False
                    SpeedLog(pingPositive, ping)
                    sleep(1)
                    linesWritten += 1
                CSVtooBig(DATA_OUTPUT_CSV_FILE_NAME) # clears out so there are only the last 24 hours left of data

    except KeyboardInterrupt:
        with open("data_output.json", "a") as writeFile:
            writeFile.write("\n}")
        logging.debug("End of program")
        print("Goodbye")
