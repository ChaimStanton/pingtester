#! python3

import csv

csvFileLIST = []
with open('data.csv', newline='') as sampleCSV:
    reader = csv.reader(sampleCSV, delimiter=',')
    for row in reader:
        csvFileLIST.insert(0, list(row))

for row in csvFileLIST:
    print("<tr>")
    for item in row:
        print("<td> <pre>" + item + "</pre> </td>")
    print("</tr>")
