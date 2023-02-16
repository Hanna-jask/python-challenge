#
import os
import csv
#dataset file path
budget_data_csv_path = os.path.join('Resources', 'budget_data.csv')

#open csv file
with open(budget_data_csv_path) as csv_file:
	csv_reader= csv.DictReader(csv_file,delimiter=',')

#defining variables
	mcount = 0
	total_profit = 0
	month_list =[]
	changes =[]
	current_profit = 0
	prevcurrent_profit = 0

#creating a loop for total months and total profit
	for row in csv_reader :
		mcount += 1
		current_profit = int(row['Profit/Losses'])
		total_profit += current_profit

#finding the change by row
		if (mcount == 1):
			prevcurrent_profit = current_profit
		else:
                        change = current_profit - prevcurrent_profit
                        month_list.append(row['Date'])
                        changes.append(change)
                        prevcurrent_profit = current_profit

#Using the change to find the average 
	sum_current_profit = sum(changes)
	av_current_profit = round(sum_current_profit/(mcount -1),2)

#using the change to find the greatest changes
	great_inc = max(changes)
	great_dec = min(changes)

#finding the corrsponding month to the greatest change
	high_m = changes.index(great_inc)
	low_m = changes.index(great_dec)
	great_inc_m = month_list[high_m]
	great_dec_m = month_list[low_m]

#printing the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {mcount}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${av_current_profit}")
print(f"Greatest Increase in Profits:{great_inc_m} (${great_inc})")
print(f"Greatest Decrease in Profits:{great_dec_m} (${great_dec})")

#exporting the results to a txt file
budget_data = os.path.join('analysis', 'budget_data.txt')
with open(budget_data, "w") as outfile:
	outfile.write ("Financial Analysis\n")
	outfile.write ("----------------------------\n")
	outfile.write (f"Total Months: {mcount}\n")
	outfile.write (f"Total: ${total_profit}\n")
	outfile.write (f"Average Change: ${av_current_profit}\n")
	outfile.write (f"Greatest Increase in Profits:{great_inc_m} (${great_inc})\n")
	outfile.write (f"Greatest Decrease in Profits:{great_dec_m} (${great_dec})\n")
