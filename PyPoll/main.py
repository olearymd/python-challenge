# 
# PyPoll Instructions
#
# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# 
# You will be given a set of poll data called election_data.csv. 
# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:
# 
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
# 6. Your analysis should look similar to the following:
# 
#     Election Results
#     -------------------------
#     Total Votes: 369711
#     -------------------------
#     Charles Casper Stockham: 23.049% (85213)
#     Diana DeGette: 73.812% (272892)
#     Raymon Anthony Doane: 3.139% (11606)
#     -------------------------
#     Winner: Diana DeGette
#     -------------------------
# 
# 7. In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# 

import os
import csv

# Initialize variable for counting votes
totalVotes = 0

# Create a voteCounts dictionary for candidates and their vote totals:
voteCounts = {}

# Set path for csv file
dataFile = os.path.join("Resources" , "election_data.csv")

# Read in the csv file
with open(dataFile, 'r', encoding="utf8") as csvFile:

    # Split data on commas
    csvReader = csv.reader(csvFile, delimiter=',')

    # Store header and continue to next row
    header = next(csvReader)

    # Iterate over each row:
    for row in csvReader:

        # Increment counter for number of votes cast
        totalVotes += 1

        # Candidate is the third field
        candidate=row[2]

        # If the candidate is not in dictionary, add candidate with an initial vote count of 1
        if candidate not in voteCounts :
            voteCounts[candidate] = 1
        
        # If the candidate is already in dictionary, increment vote count
        else:
            voteCounts[candidate] += 1

# Determine winner
winner = max(voteCounts, key=voteCounts.get)

# Iterate over each candidate in the voteCounts dictionary to get the percentage votes for that candidate and then add the percentages back to our dictionary
for candidate in voteCounts:
    percentage = round((voteCounts[candidate] / totalVotes) * 100, 2)

    # Add percentage as new item to dictionary
    voteCounts[candidate] = {'voteCounts': voteCounts[candidate], 'percentage': percentage}

# Function to get results for all candidates to print later.  Stores output in a variable called "allResults"
def getResultsForAllCandidates():
    outputList = []
    
    for candidate in voteCounts.keys():

        # Print the results to stdout, can do this.  
        # print(f"{candidate}: {voteCounts[candidate]['percentage']}% ({voteCounts[candidate]['voteCounts']})")

        # For each candidate, append a string that includes the percentage and voteCounts formatted as desired.  
        outputList.append(candidate + ": " + str(voteCounts[candidate]['percentage']) + "% (" + str(voteCounts[candidate]['voteCounts']) + ")" )

    # Join the list elements into a single variable to return
    allResults="\n".join(outputList)
    return allResults

# Run our function to get results for all candidates
allResults = getResultsForAllCandidates()

# Build a variable for outputting to stdout and a file
output=f'''
Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
{allResults}
-------------------------
Winner: {winner}
-------------------------
'''

# Print the output to stdout
print (output)

# Print the output to a file
outputFile = os.path.join("analysis" , "electionResults.txt")
with open(outputFile, 'w', encoding='utf-8') as file:
    file.write(output)
