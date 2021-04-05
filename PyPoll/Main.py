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

    #loop for each row in csv file
    for row in csv_reader:

        #add values into lists by index
        Voter_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2]) 

    Total_Votes = len(Voter_ID)
    print("Total Votes: ", Total_Votes)

    #print Khan Stats
    Num_Khan = Candidate.count("Khan")
    Khan_Pct = (Num_Khan / Total_Votes)
    Khan_Pct_Format = "{:.2%}".format(Khan_Pct)
    print("Khan: ", Khan_Pct_Format,  "(", Num_Khan, ")")

    #print Correy Stats
    Num_Correy = Candidate.count("Correy")
    Correy_Pct = (Num_Correy / Total_Votes)
    Correy_Pct_Format = "{:.3%}".format(Correy_Pct)
    print("Correy: ", Correy_Pct_Format,  "(", Num_Correy, ")")    

    #print Li Stats
    Num_Li = Candidate.count("Li")
    Li_Pct = (Num_Li / Total_Votes)
    Li_Pct_Format = "{:.3%}".format(Li_Pct)
    print("Li: ", Li_Pct_Format,  "(", Num_Li, ")")    

    #print O'Tooley Stats
    Num_Otool = Candidate.count("O'Tooley")
    Otool_Pct = (Num_Otool / Total_Votes)
    Otool_Pct_Format = "{:.3%}".format(Otool_Pct)
    print("O'Tooley: ", Otool_Pct_Format,  "(", Num_Otool, ")")  

    #Print winner with max votes
    



    Unique_Candidate = []

    for x in Candidate:
        if x not in Unique_Candidate:
                Unique_Candidate.append(x)


        
    
    