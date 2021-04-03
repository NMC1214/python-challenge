#modules
import os
import csv

#set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)

#lists to store data
Months = []

#open budget data as csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        #Total number of months included in the dataset
        TotalMonths = len(Months(csvreader))
        
print(TotalMonths)
