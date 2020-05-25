#! python3
"""This is a python file to calculate the percentages for the graph"""

import csv

numberOfTrue = 0 
numberOfFalse = 0
totalNumber =0

with open("data.csv", "r") as CSVfile:
    data = csv.reader(CSVfile)
    for row in data:
        totalNumber += 1
        if row[0] == "True":
            numberOfTrue += 1
        else:
            numberOfFalse += 1

# print(numberOfTrue/totalNumber)
# print(numberOfFalse/totalNumber)
try:
    print("[" + str(numberOfFalse/totalNumber) + "," + str(numberOfTrue/totalNumber) + "]")
except:
    print("[1, 3]")