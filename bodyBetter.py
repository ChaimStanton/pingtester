#! python3

import csv

csvFileLIST = []
with open('data.csv', newline='') as sampleCSV:
    reader = csv.reader(sampleCSV, delimiter=',')
    for row in reader:
        csvFileLIST.insert(0, list(row))
        # print(', '.join(row))

print("""
<body>
<table class="table table-light table-sm table-striped
              table-bordered  table-hover table-responsive">

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
        print("<td> <pre>" + item + "</pre> </td>")
    print("</tr>")

print("""
</tbody>
</table></body>
""")

# print(csvFileLIST)
# print("lolls")
