#Importing os module to allow creation of file paths across operating sys.
import os

#Module for reading CSV files
import csv

csvpath = os.path.join('..','python-challenge','PyPoll','Resources','election_data.csv')

#Read using CSV module
with open(csvpath) as csvfile:

    #CSV reader - delimiter
    csv_election_data = csv.reader(csvfile,delimiter=',')

    #print(csvreader)

    # Read header row first 
    csv_header = next(csv_election_data)
    #print(f"CSV Header: {csv_header}")


#####################################################################################################

    candidates = []
    voters = []
    for row in csv_election_data:
        candidates.append(row[2])
        voters.append(row[0])

total_votes_cast = (len(voters))
print(f"Total Number of votes cast: {total_votes_cast}")

#Complete List of Candidates who received votes
candidates_set = set(candidates)
new_candidates_list = list(candidates_set)
print(f"Candidates who received votes: {new_candidates_list}")

#Percentage of Votes Each Candidate Won





