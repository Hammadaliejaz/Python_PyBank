# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("Resources", "election_data.csv")


# Import Dependencies
import os, csv
from pathlib import Path

# Declaring file path location
input_file = Path("python-challenge", "pyroll", "election_data.csv")


# Open csv in default read mode with context manager
with open("election_data.csv") as budget:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget,delimiter=",")

    # Skip the header labels to iterate with the values
    header = next(csvreader)
 # Declare Variables
 total_votes = 0
 khan_votes = 0
 correy_votes = 0
 li_votes = 0
 otooley_votes = 0
 # Count the unique Voter ID's and store in variable  called total_votes
total_votes +=1

  # Making list for all the four participants
if row[2] == "Khan":
khan_votes +=1
elif row[2] == "Correy":
correy_votes +=1
elif row[2] == "Li":
li_votes +=1
elif row[2] == "O'Tooley":
otooley_votes +=1

# Creating a dictionart out of the two lists we created
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# We zip them together the list of candidate(key) and the total votes(value) and declare winner using a max function
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
print(f"election results)
khan_percent = (khan_votes/total_votes) *100
print(f"total_votes:{khan_votes})
correy_percent = (correy_votes/total_votes) * 100
print(f"total votes:{correy_votes})
li_percent = (li_votes/total_votes)* 100
print (f"Li_votes)
otooley_percent = (otooley_votes/total_votes) * 100
print(f"ootoley_votes:{ootoley_votes})

print(f"winner:{key})    
