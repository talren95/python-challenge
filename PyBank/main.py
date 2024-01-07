import os
import csv

# Path to show where to collect information from
budget_data_csv = os.path.join(".." , "PyBank" , "Resources" , "budget_data.csv")
# Setting the variables
total_months = 0

# Total number of months in the dataset
# Open and read the csv flie
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Reading/Skipping the header row
    header = next(csv_reader, None)

    # Reading the first row (there is no header)
    for row in csv_reader:

        total_months += 1

# Display the total number of months
print(f"Total months: {total_months}")


# Net Total Amount of Profit/Losses
# Setting the variables
net_total = 0

# Open and read the csv file
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Reading/Skipping the header row
    header = next(csv_reader, None)
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        profit_loss = int(row[1])
        
        # Add the Profit/Losses value to the net_total
        net_total += profit_loss

# Display the net total of Profit/Losses
print(f"Total: {net_total}")


# Changes in Profit/Losses
# Setting the variables
changes = []
previous_profit_loss = None

# Open and read the csv file
with open(budget_data_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Read header row
    header = next(csv_reader, None)
    
    # Loop through each row in the csv file
    for row in csv_reader:
        profit_loss = int(row[1])
        
        # Calculate the changes from previous
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
        
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes)

# Display the average change
print(f"Average change: {average_change}")

# Greatest increase and decrease in profits
# Setting the variables
dates = []

# Open and read the csv file
with open(budget_data_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Read the header
    header = next(csv_reader, None)
    
    # Loop through the csv file
    for row in csv_reader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Store the date
        dates.append(date)

# Find the greatest increase and decrease in profits with dates
greatest_increase = max(changes) if changes else 0
greatest_decrease = min(changes) if changes else 0

# Find the dates associated with greatest increase and decrease
date_of_increase = dates[changes.index(greatest_increase)] if greatest_increase != 0 else None
date_of_decrease = dates[changes.index(greatest_decrease)] if greatest_decrease != 0 else None

# Display the results
print(f"Greatest increase: {date_of_increase} ({greatest_increase})")
print(f"Greatest decrease: {date_of_decrease} ({greatest_decrease})")
