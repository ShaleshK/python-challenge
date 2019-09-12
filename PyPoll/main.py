# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
count = 0
for line in open(csvpath).xreadlines(  ): count += 1
column = 1
total_votes = sum(row[column] for row in csvpath)

print("Election Results")
print("----------------------------")
printf("Total Votes: " str(count))
print("----------------------------")
