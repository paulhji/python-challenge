import os
import csv
from pathlib import Path
csvpath = os.path.join("C:/Users/Matthew/Desktop/DU Analytics Course Work/Pandas - 2/Module 3 Challenge/Starter_Code/PyBank/Resources/budget_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

# Create lists to go through each row for following variables
total_months = []
total_profit = []
monthly_profit_change = []

# Open csv file
with open(csvpath,newline="", encoding="utf-8") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)

# Go through each row and fill in each list
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
            
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# Calculate the greatest increase and decrease (max and min) in profits (date and amount) over the entire period
    greatest_profit_increase=max(monthly_profit_change)
    greatest_profit_decrease=min(monthly_profit_change)
    
# Put these into lists and index from max to min
    max_increase_month=monthly_profit_change.index(max(monthly_profit_change)) + 1
    max_decrease_month=monthly_profit_change.index(min(monthly_profit_change)) + 1
    
print('Financial Analysis')
print('------------------------')
print(f'Total Months: {len(total_months)}')
print(f"Total: ${sum(total_profit)}")
print(f'Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}')
print(f'Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(greatest_profit_increase))})')
print(f'Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(greatest_profit_decrease))})')
                         
# Output analysis to file
output_file = Path('C:/Users/Matthew/Desktop/DU Analytics Course Work/Pandas - 2/Module 3 Challenge/Starter_Code/PyBank/Resources/Financial_Analysis.txt')

# Write text to output file
with open(output_file, 'w') as file:
    file.write('Financial Analysis')
    file.write('\n')
    file.write('------------------------')
    file.write('\n')
    file.write(f'Total Months: {len(total_months)}')
    file.write('\n')
    file.write(f"Total: ${sum(total_profit)}")
    file.write('\n')
    file.write(f'Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}')
    file.write('\n')
    file.write(f'Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(greatest_profit_increase))})')
    file.write('\n')
    file.write(f'Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(greatest_profit_decrease))})')
