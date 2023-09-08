import os
import csv
from datetime import datetime, timedelta

# Define the path to the CSV file
csv_path = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
unique_names = set()
candidate_votes = {}  # Dictionary to store candidate votes
winner = ""
max_votes = 0

# Read and process the CSV file
with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row
    for row in csvreader:
        # Extract ID, County, Candidate from the row
        ID_str, county_str, candidate_str = row
        # Update total votes
        total_votes += 1
        # Add the candidate name to the set of unique names
        unique_names.add(candidate_str)
        # Update candidate vote count
        if candidate_str in candidate_votes:
            candidate_votes[candidate_str] += 1
        else:
            candidate_votes[candidate_str] = 1

# Convert the set back to a list to get the unique candidate names
unique_names_list = list(unique_names)

print("Election Results")
print("----------------------------")
print(f"Total total_votes: {total_votes}")
print("----------------------------")

# Loop through the candidates and calculate their percentage of votes
for candidate in unique_names:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Check if this candidate has the most votes so far
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print("----------------------------")
print(f"Winner: {winner}") 
print("----------------------------")

# Create a text file to write the results
output_path = r"C:\Users\qianc\Desktop\BootCamp\Course\Assignments\Module 3\python_challenge\PyPoll\analysis\Election_Results.txt"
with open(output_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("----------------------------\n")

    # Loop through the candidates and calculate their percentage of votes
    for candidate in unique_names_list:
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        # Check if this candidate has the most votes so far
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    output_file.write("----------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("----------------------------\n")

print("Results have been written to 'election_results.txt'.")