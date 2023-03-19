 # Import module that allows us to read across operating systems and the module that allows the user to read csv files
import os, csv


cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

PB_file = "Resources"
csvpath = os.path.join(PB_file , 'budget_data.csv')

# Open the csvpath as a csv file
with open(csvpath, 'r') as csvfile:
      
    #Open file as a Dictionary form to map information in each row as a dict
    csvreader = csv.DictReader(csvfile, delimiter=',')

    # Set variable needed for this script. Inc and dec will store 2 types of variables (date and change in revenue)
    totals = 0
    change = 0
    prev_rev = 0
    total_ch = 0
    inc = ["",0]
    dec = ['',0]

    # Use enumerate to the number of rows with iterable sequences and skip the header row
    for row_count, row in enumerate(csvreader, start=1):
        rev = int(row['Profit/Losses'])
        
        # Determine the total revenue across the period
        totals += rev
        
        # Determine the changes in revenue across each month so that the average change in revenus can be calculated
        change = rev - prev_rev
        prev_rev = rev 

        if row_count == 1:
             change = 0
        
        total_ch += change
        
        # Determine the greatest increase in profits by looping through the column
        if (change > inc[1]):
             inc[1] = change
             inc[0] = row["Date"]

        # Now do the same for the biggest decrease by also looping through   
        if (change < dec[1]):
            dec[1] = change
            dec[0] = row["Date"]

# Print the output of this script into the terminal
output = f'''
Financial Analysis
----------------------------
Total Months: {row_count}
Total: ${totals:,}
Average Change: ${total_ch/(row_count - 1):,.2f}
Greatest Increase in Profits: {inc[0]} (${inc[1]})
Greatest Decrease in Profits: {dec[0]} (${dec[1]})
'''

print(output)

# Save the output of the script as a text file in the Analysis Folder.   
output_file = os.path.join("Analysis", "Analysis.txt")

# Open the output folder
with open(output_file, "w") as text_file:
        text_file.write(output)
os.startfile("Analysis")     

