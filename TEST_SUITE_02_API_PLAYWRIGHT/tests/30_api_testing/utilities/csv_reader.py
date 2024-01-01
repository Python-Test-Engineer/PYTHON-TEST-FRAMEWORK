import csv
from boxen import bx_info, bx_result

with open("../data/loanapp.csv") as f:
    csv_reader = csv.reader(f, delimiter=",")
    print(csv_reader)
    # print(list(csv_reader))
    for row in csv_reader:
        bx_result(str(row))
