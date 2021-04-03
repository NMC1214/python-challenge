#modules
import os
import csv

#set path for file
csvpath = os.path.join("PyPoll","Resources","election_data.csv")
print(csvpath)

#open budget data as csvfile
with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    


