import os
import csv

trail = os.path.join("Resources", "election_data.csv")


voters = []
runners = []
outputstring = ""

with open (trail) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        voters.append(row[0])
        runners.append(row[2])
    
    print("Election Results:")
    outputstring += "Election Results:\n"
    print("------------------------")
    outputstring += ("------------------------\n")
    print("Total Votes: " + (str(len(voters))))
    outputstring += ("Total Votes: " + (str(len(voters)))) + "\n"
    print("------------------------")
    outputstring += ("------------------------\n")

unique = list(set(runners))
votes = []
percents = []


for name in unique:
    votecount = runners.count(name)
    votes.append(votecount)
    percent = votecount/len(runners)
    percents.append(percent)
    print(name + ":" + " " + str("{:0.00%}".format(percent) + " (" + str(votecount)) + ")")
    outputstring += name + ":" + " " + str("{:0.00%}".format(percent) + " (" + str(votecount)) + ")\n"
    
winner = unique[votes.index(max(votes))]
print("------------------------")
outputstring += "------------------------\n"
print("Winner: " + (winner))
outputstring += ("Winner: " + (winner) + "\n") 
print("------------------------")
outputstring += "------------------------\n"

election_output_file = os.path.join("analysis", "results.txt")
with open (election_output_file, "w") as datafile:
#     datafile.write("Election Results: \n")
#     datafile.write("------------------------\n")
#     datafile.write("Total Votes: " + (str(len(voters))) + "\n")
#     datafile.write("------------------------\n")
#     datafile.write((name) + ":" + " " + str("{:0.00%}".format(percent) + " (" + str(votecount)) + ")\n")
#     datafile.write("------------------------\n")
#     datafile.write("winner: " + (winner) + "\n")
#     datafile.write("------------------------\n")
    datafile.write(outputstring)