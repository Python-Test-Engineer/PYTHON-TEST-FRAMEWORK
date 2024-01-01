import csv

with open("./data/loanapp.csv") as f:
    csv_reader = csv.reader(f, delimiter=",")
    print(csv_reader)
    print(list(csv_reader))
    names = []
    stats = []
    for row in csv_reader:
        names.append(row[0])
        stats.append(row[1])

print(names)
print(stats)
