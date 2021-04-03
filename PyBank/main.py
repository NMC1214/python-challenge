#modules
import os
import csv

#set path for file
csvpath = os.path.join("PyBank","Resources","budget_data.csv")
print(csvpath)

#open budget data as csvfile
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    #Skip header row
    next(csv_reader)

    #Create list of Profit/Losses Values
    Sum_Profit = []
    for line in csv_reader:
 
        Sum_Profit.append(line[1])
        Profit_floats = [float(item) for item in Sum_Profit]

    #Print first profit value
    print(Profit_floats[0])

    #print last profit value
    print(Profit_floats[85])

    print(type(Profit_floats[1]))

    print("Total Months: ",len(Profit_floats))

    #net total amount of "Profit/Losses" over the entire period
    Sum_Values = sum(Profit_floats)
    print("Total: ",Sum_Values)

    #return max value
    Largest_Profit = max(Profit_floats)
    print("Largest Profit Value: ",Largest_Profit)

    #return smallest value
    Largest_Loss = min(Profit_floats)
    print("Biggest Loss: ",Largest_Loss)





            



    
