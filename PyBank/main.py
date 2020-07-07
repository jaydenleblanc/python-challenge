#Importing os module to allow creation of file paths across operating sys.
import os

#Module for reading CSV files
import csv

csvpath = os.path.join('..','python-challenge','PyBank','Resources','budget_data.csv')

#Read using CSV module
with open(csvpath) as csvfile:

    profit_change = 0

    #CSV reader - delimiter
    csvreader = csv.reader(csvfile,delimiter=',')

    #print(csvreader)

    # Read header row first 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


#####################################################################
    
    months = []
    profit_losses = []
    average_changes = []

    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
    
    #Iterate the profit_losses list and set variable to difference. Then add each difference to average_changes list
    i = 0
    for i in range(len(profit_losses) -1):
        profit_change = int(profit_losses[i+1]) - int(profit_losses[i]) 
        average_changes.append(profit_change)
    
    
    total = (sum(profit_losses))
    average_profit_change = (sum(average_changes)/len(average_changes))
    formatted_average_change = ("{:.2f}".format(average_profit_change))
    

    #Greatest Increase in profits (date & amount) MAX
    max_index = average_changes.index(max(average_changes))
    greatest_increase_month = months[max_index]
    greatest_increase_amount = average_changes[max_index]
    #print(max_index)
    
    #Greatest Decrease in profits (date & amount) MIN
    min_index = average_changes.index(min(average_changes))
    greatest_decrease_month = months[min_index]
    greatest_decrease_amount = average_changes[min_index]
    #print(min_index)



    print("Financial Analysis")
    print("***************************")
    print("Total Number of Months in the Dataset:")
    print(len(months))
    print("Net Total Amount:")
    print(f"${total}")
    print("Average Change in Profit/Losses:")
    print(f"${formatted_average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase_amount}")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease_amount}")

    f = open("finalresults.txt", "a")
    print("Financial Analysis", file=f)
    print("***************************", file=f)
    print("Total Number of Months in the Dataset:", file=f)
    print(len(months), file=f)
    print("Net Total Amount:", file=f)
    print(f"${total}", file=f)
    print("Average Change in Profit/Losses:", file=f)
    print(f"${formatted_average_change}", file=f)
    print(f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase_amount}", file=f)
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease_amount}", file=f)
    
    f.close()




    






    


        




