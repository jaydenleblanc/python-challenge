#Importing os module to allow creation of file paths across operating sys.
import os

#Module for reading CSV files
import csv

csvpath = os.path.join('..','python-challenge','PyBank','Resources','budget_data.csv')

#Read using CSV module
with open(csvpath) as csvfile:

    #CSV reader - delimiter
    csvreader = csv.reader(csvfile,delimiter=',')

    print(csvreader)

    # Read header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Print total number of months included in the dataset
    
    
    
    
    
    
    #Read each row of data after the header
    for row in csvreader:
        print(row)

        