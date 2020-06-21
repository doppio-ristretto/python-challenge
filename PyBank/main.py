import os
import csv

moneytrail = os.path.join("resources", "budget_data.csv")

months = []
profit_losses = []
change = []
updowntotal = 0

with open (moneytrail) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
        updowntotal += int(row[1])

i = 0
while i < len(profit_losses) - 1:
    change.append(profit_losses[i+1]-profit_losses[i])
    i = i + 1

totalmonths = len(months)
avgchange = round((sum(change)/len(change)),2)
bigups = max(change)
bigdowns = min(change)

print("Financial Analysis")
print("----------------------------------")
print("Total Months: " + str(totalmonths))
print("Total: $" + str(updowntotal))
print("Average Change: $" + str(avgchange))
print("Greatest Increase in Profits: $" + str(bigups))
print("Greatest Decrease in Profits: $" + str(bigdowns))

analysis_output_file = os.path.join("analysis", "results.txt")
with open(analysis_output_file, "w") as datafile:
    datafile.write("Financial Analysis \n")
    datafile.write("----------------------------------\n")
    datafile.write("Total Months: " + str(totalmonths)+ "\n")
    datafile.write("Total: $" + str(updowntotal)+ "\n")
    datafile.write("Average Change: $" + str(avgchange)+ "\n")
    datafile.write("Greatest Increase in Profits: $" + str(bigups)+ "\n")
    datafile.write("Greatest Decrease in Profits: $" + str(bigdowns))