import os
import csv

# Path to show where to collect information from
election_data_csv = os.path.join(".." , "PyPoll" , "Resources" , "election_data.csv")
# Setting the variables
total_votes = 0
candidate_votes = {}

# Total number of votes
# Open and read the csv flie
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Reading/Skipping the header row
    header = next(csv_reader, None)

    # Reading the first row after the header
    for row in csv_reader:

        total_votes += 1
        candidate_name = row[2]

        # Counting the votes for each candidate
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Calculating for the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Display the total number of votes
print(f"Total Votes: {total_votes}")
print("---------------------------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate} {percentage: .2f}% ({votes})")
print("---------------------------------------------")
print (f"Winner: {winner}")