# 

# In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
# You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses". 
# (Thankfully, your company has rather lax standards for accounting, so the records are simple.)
# 
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# 
#   1. The total number of months included in the dataset
#   2. The net total amount of "Profit/Losses" over the entire period
#   3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
#   4. The greatest increase in profits (date and amount) over the entire period
#   5. The greatest decrease in profits (date and amount) over the entire period
#   6. Your analysis should look similar to the following:
# 
#       Financial Analysis
#       ----------------------------
#       Total Months: 86
#       Total: $22564198
#       Average Change: $-8311.11
#       Greatest Increase in Profits: Aug-16 ($1862002)
#       Greatest Decrease in Profits: Feb-14 ($-1825558)
#    
#   7. In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# 

import os
import csv

# Initialize variables
monthsCount = 0
netProfit = 0
prevProfit = None
delta = 0
deltaList = []
greatestIncrease = 0
greatestDecrease = 0

# Set path for csv file
dataFile = os.path.join("Resources" , "budget_data.csv")

# Read in the budget_data.csv 
with open(dataFile, 'r', encoding="utf8") as csvFile:

    # Split data on commas
    csvReader = csv.reader(csvFile, delimiter=',')

    # Store header and continue to next row 
    header = next(csvReader)

    # Iterate over each row:
    for row in csvReader:

        # Print the entire row:
        # print(row)
     
        # Increment counter for number of months
        monthsCount = monthsCount + 1

        # Sum the profits/losses
        netProfit = netProfit + int(row[1])

        # Find changes in profit/losses over the entire period
        profit = int(row[1])

        # If this is the first entry, there won't be a previous profit, so test if it's set to "None"
        if prevProfit != None :
            delta = profit - prevProfit
            # Create a list of our deltas, so we can average them later 
            deltaList.append(delta)

        # Test if delta is greater than greatestIncrease.  If it is, set greatestIncrease to delta
        if delta > greatestIncrease :
            greatestIncrease = delta
            greatestIncreaseMonth = row[0]
            
        # Test if delta is less than greatestDecrease.  If it is, set greatestDecrease to delta
        if delta < greatestDecrease :
            greatestDecrease = delta
            greatestDecreaseMonth = row[0]

        # update prevProfit before next entry into loop
        prevProfit = profit

# Once out of the loop, get the average of our deltas, and then round them to 2 digits.
deltaAverage = sum(deltaList) / len(deltaList)
deltaAverage = round(deltaAverage, 2)

# Build output variable
output = f"""Financial Analysis
----------------------------
Total Months: {monthsCount}
Total: ${netProfit}
Average Change: ${deltaAverage}
Greatest Increase in Profits: {greatestIncreaseMonth} (${greatestIncrease})
Greatest Decrease in Profits: {greatestDecreaseMonth} (${greatestDecrease})
"""

# Print the output to stdout
print (output)

# Print the output to a file
outputFile = os.path.join("analysis" , "financialAnalysis.txt")
with open(outputFile, 'w', encoding='utf-8') as file:
    file.write(output)

# print(f"CSV file contents: {csvReader}") 
