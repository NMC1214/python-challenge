#modules
import os
import csv

#set path for file
csvpath = os.path.join("PyBank","Resources","budget_data.csv")
print(csvpath)

#open budget data as csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #read header row
    csv_header = next(csvreader)

    #Count Number Months
    Months = list(csvreader)
    Total_Months = len(Months)
    print(Total_Months)

    #Sum of "profit/loses" over the entire period
