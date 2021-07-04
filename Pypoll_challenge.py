#add our dependencies
import csv
import os

#add a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
print(file_to_load)
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

#candidate options and candidate votes
candidate_options = []
candidate_vote = {}

