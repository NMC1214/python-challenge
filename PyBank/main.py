#modules
import os
import csv

#set path for file
csvpath = os.path.join("PyBank","Resources","budget_data.csv")

#open budget data as csvfile
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    Months = []
    Profit = []
    Profit_Change = []

    for row in csv_reader:

        Months.append(row[0])

        Profit.append(int(row[1]))

    Total_Months = len(Months)
    print("Total Months: ", Total_Months)

    Total_Profit = sum(Profit)
    print("Total: $", Total_Profit)

    for i in range(len(Profit)-1):
        Profit_Change.append(Profit[i+1]-Profit[i])

    Average_Change = sum(Profit_Change) / len(Profit_Change)

    print("Average Change: $", Average_Change)

    Great_Inc = max(Profit_Change)
    print("Greatest Increase in Profits: ", "($",Great_Inc,")")

    Great_Loss = min(Profit_Change)
    print("Greatest Decrease in Profits: ", "($", Great_Loss, ")")
        






            



    
