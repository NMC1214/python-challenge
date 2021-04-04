#modules
import os
import csv

#set path for file
csvpath = os.path.join("PyPoll","Resources","election_data.csv")
print(csvpath)

#open budget data as csvfile
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skip header line
    csv_header = next(csv_reader)

    #create lists of data
    Voter_ID = []
    County = []
    Candidate = []
    Khan_Votes = []
    Correy_Votes = []
    Li_Votes = []
    OTool_Votes = []

    #loop for each row in csv file
    for row in csv_reader:

        #add values into lists by index
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2]) 

    Num_Khan = Candidate.count("Khan")
    print(Num_Khan)

    Total_Votes = len(Voter_ID)
    print("Total Votes: ", Total_Votes)


    Unique_Candidate = []

    for x in Candidate:
        if x not in Unique_Candidate:
                Unique_Candidate.append(x)

    print(Unique_Candidate)

        
    
    