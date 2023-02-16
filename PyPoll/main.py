#read csv
import os
import csv

#dataset file path
election_data_csv = os.path.join('Resources','election_data.csv')

#open csv file
with open(election_data_csv) as csv_file:
	csv_reader= csv.DictReader(csv_file,delimiter=',')
	
#Defining  variables
	total_votes = 0
	CCS = 0
	DD = 0
	RAD = 0
	options = []
	candiates = []
	no_votes_candidates = []

#creating loop to find total votes and append rows in candiates column
	for row in csv_reader :
		total_votes += 1
		candiates.append(row['Candidate'])
#counting no. votes by candiate
	CCS = candiates.count('Charles Casper Stockham') 
	DD = candiates.count('Diana DeGette')
	RAD = candiates.count('Raymon Anthony Doane')
	
# % no. votes by candiate
	CCSP = round((CCS / total_votes *100),3)
	DDP = round((DD / total_votes *100),3)
	RADP = round((RAD / total_votes *100),3)

#finding the winner of the election
	options_n = ["Charles Casper Stockham","Raymon Anthony Doane", "Diana DeGette"]
	options_v = [CCS, RAD, DD]
	options_dic = dict(zip(options_n,options_v))
	winner = max(options_dic, key=options_dic.get)


#printing the results
print("Election Votes")
print("----------------------------")
print(f"Total Votes:{total_votes} ")
print("----------------------------")
print(f"Charles Casper Stockham: {CCSP}% ({CCS})")
print(f"Diana DeGette: {DDP}% ({DD})")
print(f"Raymon Anthony Doane: {RADP}% ({RAD})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

#exporting results into a txt file
election_data = os.path.join('analysis', 'election_data.txt')
with open(election_data, "w") as outfile:

	outfile.write ("Election Votes\n")
	outfile.write ("----------------------------\n")
	outfile.write (f"Total Votes:{total_votes} \n")
	outfile.write ("----------------------------\n")
	outfile.write (f"Charles Casper Stockham: {CCSP}% ({CCS})\n")
	outfile.write (f"Diana DeGette: {DDP}% ({DD})\n")
	outfile.write (f"Raymon Anthony Doane: {RADP}% ({RAD})\n")
	outfile.write ("----------------------------\n")
	outfile.write (f"Winner: {winner}\n")
	outfile.write ("----------------------------\n")
