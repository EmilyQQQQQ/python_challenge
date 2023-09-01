import os
import csv

# "..",  this is to go back one level
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    print(header)
    for row in csvreader:
        Date = row[0]
        PL = int(row[1])
        #print(PL)
    
    