#modules
import os
import csv

#set path for file
csvpath = os.path.join("PyBank","Resources","budget_data.csv")

#open budget data as csvfile
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skip header line
    csv_header = next(csv_reader)

    #create lists for data
    Months = []
    Profit = []
    Profit_Change = []

    #loop for each row in csvfile
    for row in csv_reader:

        #add first column to Month list
        Months.append(row[0])

        #add profit/loss to profit list
        Profit.append(int(row[1]))

    #number items in months list
    Total_Months = len(Months)
    print("Total Months: ", Total_Months)

    #sum of profit list
    Total_Profit = sum(Profit)
    print("Total: $", Total_Profit)

    #loop for profit list
    for i in range(len(Profit)-1):

        #subtract next item in list from current item
        Profit_Change.append(Profit[i+1]-Profit[i])

    #divide total of profit change list by items in the list to tell average
    Average_Change = sum(Profit_Change) / len(Profit_Change)
    print("Average Change: $", Average_Change)

    #find largest change in list
    Great_Inc = max(Profit_Change)
    #find index of the item in list with largest change
    max_Inc_index = Profit_Change.index(Great_Inc)
    print("Greatest Increase in Profits: ", Months[(max_Inc_index + 1)], "($",Great_Inc,")")

    #find smallet item in change list
    Great_Loss = min(Profit_Change)
    #find index of that item
    max_Dec_index = Profit_Change.index(Great_Loss)
    print("Greatest Decrease in Profits: ", Months[(max_Dec_index + 1)], "($", Great_Loss, ")")

    text_path = os.path.join("PyBank","Analysis", "Financial_Analysis.txt")
    f = open(text_path, "w")

    print("Financial Analysis", file=f)
    print("---------------------------------", file=f)
    print(("Total Months: ", Total_Months), file=f)
    print(("Total: $", Total_Profit), file=f)
    print(("Average Change: $", Average_Change), file=f)
    print(("Greatest Increase in Profits: ", Months[(max_Inc_index + 1)], "($",Great_Inc,")"), file=f)
    print(("Greatest Decrease in Profits: ", Months[(max_Dec_index + 1)], "($", Great_Loss, ")"), file=f)

    f.close()







            



    
