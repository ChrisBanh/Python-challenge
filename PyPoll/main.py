 # Import module that allows us to read across operating systems and the module that allows the user to read csv files
import os, csv


cwd = os.getcwd()

PP_file = "Resources"

pollpath = os.path.join(PP_file , 'election_data.csv')


with open(pollpath) as csvfile:
  data = csv.reader(csvfile, delimiter=',')

  # Read the header row to skip it 
  csv_header = next(csvfile)
  # Set the variable for row count as this will determine the total number of votes
  row_count = 0

  # Set this varaible as a dictionary so that it can count the number of times a name has been read and tally them up.
  candvotes = {}

   
  for row in data:
    
    # Tally up the total number of votes within this dataset.
    row_count += 1 

    if row[2] not in candvotes.keys():
             
      candvotes[row[2]] = 1
    else:
      candvotes[row[2]] += 1

# Get the percentage of votes and print result next to candidate and total votes. Combine strings through .join to create a varaible that list all of the candidates and their respective number of votes. 

candidates_list = ""
for candidate in candvotes.keys():
  candidates_list =  '\n'.join([candidates_list, candidate + " {:.3%}".format(candvotes[candidate] / row_count) + " (" + str(candvotes[candidate])+ ")"])

#Grab the winner by determine the max number of times a name has been mentioned within this dataset.
winner = max(candvotes, key=candvotes.get)


output = f'''
Election Results
-------------------------
Total Votes: {row_count}
-------------------------
{candidates_list}
-------------------------
Winner: {winner}
-------------------------
'''
# Print the output into the terminal
print(output)

 

# Print the output as a text file into a designated folder.
output_file = os.path.join("Analysis", "Analysis.txt")

    #  Open the output folder
with open(output_file, "w") as text_file:
        text_file.write(output)
os.startfile("Analysis")