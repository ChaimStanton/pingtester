#! python3

import sys
import csv
from tabulate import tabulate

csvFileLIST = []
with open('data.csv', newline='') as sampleCSV:
    reader = csv.reader(sampleCSV, delimiter=',')
    for row in reader:
        csvFileLIST.append(list(row))
        # print(', '.join(row))

print("""
<body>
<table class="table table-light table-sm table-striped table-bordered table-hover">

<thead class="thead-light">
        <tr>
        <th scope="col">status</th>
        <th scope="col">remark</th>
        <th scope="col">time (day/month/year hour/minute/second)</th>
        </tr>
</thead>

<tbody>
""")

for row in csvFileLIST:
    print("<tr>")
    for item in row:
        print("<td>" + item +"</td>")
    print("</tr>")

print("""
</tbody>
</table></body>
""")

# print(csvFileLIST)
# print("lolls")

