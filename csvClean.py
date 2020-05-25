#! python3
"""This exists purely as a utility if the server running this program is to be updated"""

import csv

from speedtest import CSVtooBig

if __name__ == "__main__":
    CSVtooBig("data.csv")
    print("CSV file has been reduced in size thank you and goodbye")
