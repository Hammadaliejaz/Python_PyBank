#import os
import os

# Reading CSV files
import csv

csvpath = os.path.join("Resources", "budget_data.csv")


# Import Dependencies
import os, csv
from pathlib import Path

# Declaring file path location
input_file = Path("python-challenge", "PyBank", "budget_data.csv")


# Open csv in default read mode with context manager
with open("budget_data.csv") as budget:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget,delimiter=",")

    # Skip the header labels to iterate with the values
    header = next(csvreader)

    # Iterate through the rows in the stored file contents
    for row in csvreader:
# iteriating through rows variable
    total_months =[]
    total_profit =[]
    monthly_profit_change =[]

# Adding total months and total profit
total_months.append(row[0])
total_profit.append(int(row[1]))

    # calculating monthly profit change
    for i in range(len(total_profit)-1):

        # difference in the two months and add the monthly change between the two months
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# Calculating the minimun and maximum change in monthly profit list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# Obtaining the maximum and minimum of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1
