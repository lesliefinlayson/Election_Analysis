#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

import csv
import os

#assign a variable for the file to load adn the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#assign a variable to save the file to a path.
file_to_save = os.path.join("analaysis", "election_analysis.txt")

#Open the elction results and read the file.
with open(file_to_load) as election_data:
 
#to do:read and analyze data
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)
    print(headers)

