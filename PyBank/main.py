#modules
import os
import csv

#set path for file
csvpath = os.path.join("PyBank","Resources","budget_data.csv")
print(csvpath)

#open budget data as csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")