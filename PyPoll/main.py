#Importing os module to allow creation of file paths across operating sys.
import os

#Module for reading CSV files
import csv

csvpath = os.path.join('..','python-challenge','PyPoll','Resources','election_data.csv')

#Import Counter Subclass from collections module to be able to count votes from list
from collections import Counter

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

#Complete List of Candidates who received votes (return unique values only using 'set' data type)
candidates_set = set(candidates)
new_candidates_list = list(candidates_set)

#Count number of votes for each candidate (how many times the name appears in the list) Result is a dictionary
votes_counted = Counter(candidates)

#Find Candidate with the most votes by converting to a list
winner = max(votes_counted.values())
final_list = [i for i in votes_counted.keys() if votes_counted[i]== winner]


print("Election Results")
print("-----------------------------------")
print(f"Total Number of votes cast: {total_votes_cast}")
print("-----------------------------------")

#Calculate Percentage for each candidate
sum_votes_counted = sum(votes_counted.values())
for k,v in votes_counted.items():
    percentage = v * 100.0 / sum_votes_counted
    print(f" {k}:{percentage}% ({v})")
print("------------------------------------")
print("The Winner of the Election is:")
print(sorted(final_list)[0])



#Print to text file
f = open("finalresults.txt", "a")
print("Election Results", file=f)
print("-----------------------------------", file=f)
print(f"Total Number of votes cast: {total_votes_cast}", file=f)
print("-----------------------------------", file=f)

#Calculate Percentage for each candidate
sum_votes_counted = sum(votes_counted.values())
for k,v in votes_counted.items():
    percentage = v * 100.0 / sum_votes_counted
    print(f" {k}:{percentage}% ({v})", file=f)
print("------------------------------------", file=f)
print("The Winner of the Election is:", file=f)
print(sorted(final_list)[0], file=f)




