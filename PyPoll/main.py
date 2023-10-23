import os
from pathlib import Path

import csv
csvpath = os.path.join('C:/Users/Matthew/Desktop/DU Analytics Course Work/Pandas - 2/Module 3 Challenge/Starter_Code/PyPoll/Resources/election_data.csv')

# Declare the variables
total_votes = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0

with open(csvpath, encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Identify Candidates who received votes and calculate how many votes they received
    for row in csvreader:

        # Calculate Total Votes
        total_votes +=1

        # Store candidate votes in a list
        if row[2] == 'Charles Casper Stockham':
            stockham_votes +=1
        elif row[2] == 'Diana DeGette':
            degette_votes +=1
        elif row[2] == 'Raymon Anthony Doane':
            doane_votes +=1

            
# Create a list of candidates and votes 
candidates = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
votes = [stockham_votes, degette_votes, doane_votes]


# Identify the winner using the dictionary and returning with max function
dict_candidates_and_votes= dict(zip(candidates, votes))
key = max(dict_candidates_and_votes, key = dict_candidates_and_votes.get)


# Calculate Percentage of Votes Each Candidate Won
stockham_percent = (stockham_votes/total_votes) * 100
degette_percent = (degette_votes/total_votes) * 100
doane_percent = (doane_votes/total_votes) * 100


# Output data to verity
print(f'Election Results')
print(f'----------------------------------------')
print(f'Total Votes: {total_votes}')
print(f'----------------------------------------')
print(f'Charles Casper Stockham: {stockham_percent:.2f}% ({stockham_votes})')
print(f'Diana DeGette: {degette_percent:.2f}% ({degette_votes})')
print(f'Raymon Anthony Doane: {doane_percent:.2f}% ({doane_votes})')
print(f'-----------------------------------------')
print(f'Winner: {key}')
print(f'-----------------------------------------')


# Output to text file
output_file = Path('C:/Users/Matthew/Desktop/DU Analytics Course Work/Pandas - 2/Module 3 Challenge/Starter_Code/PyPoll/Resources/Election_Results.txt')

with open(output_file,'w') as file:

    file.write(f'Election Results')
    file.write('\n')
    file.write(f'---------------------------------------')
    file.write('\n')
    file.write(f'Total Votes: {total_votes}')
    file.write('\n')
    file.write(f'---------------------------------------')
    file.write('\n')
    file.write(f'Charles Casper Stockham: {stockham_percent:.2f}% ({stockham_votes})')
    file.write('\n')
    file.write(f'Diana DeGette: {degette_percent:.2f}% ({degette_votes})')
    file.write('\n')
    file.write(f'Raymon Anthony Doane: {doane_percent:.2f}% ({doane_votes})')
    file.write('\n')
    file.write(f'---------------------------------------')
    file.write('\n')
    file.write(f'Winner: {key}')
    file.write('\n')
    file.write(f'---------------------------------------')
