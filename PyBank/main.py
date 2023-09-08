import os
import csv
from datetime import datetime, timedelta

# Define the path to the CSV file
csv_path = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
total_pl = 0
monthly_changes = []
date_obj = []
previous_month_pl = None

# Read and process the CSV file
with open(csv_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row
    for row in csvreader:
        # Extract date and profit/loss from the row
        date_str, pl_str = row
        date_obj.append(datetime.strptime(date_str, "%b-%y"))
        profit_loss = int(pl_str)

        # Update total months and total profit/loss
        total_months += 1
        total_pl += profit_loss

        # Calculate monthly change
        if previous_month_pl is not None:
            monthly_change = profit_loss - previous_month_pl
            monthly_changes.append(monthly_change)

        previous_month_pl = profit_loss

# Calculate the average change
average_monthly_change = sum(monthly_changes) / len(monthly_changes)

# Define the path to the output text file
output_path = r"C:\Users\qianc\Desktop\BootCamp\Course\Assignments\Module 3\python_challenge\PyBank\analysis\Financial_Analysis.txt"

# Write the results to the output text file
with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total Profit/Loss: ${total_pl}\n")
    output_file.write(f"Average Change: ${average_monthly_change:.2f}\n")

    # Calculate and write other required metrics
    # (You can add these calculations and writes if needed)

    # Find the greatest increase and decrease in profits and their corresponding months
    max_increase = max(monthly_changes)
    max_decrease = min(monthly_changes)
    max_increase_index = monthly_changes.index(max_increase)
    max_decrease_index = monthly_changes.index(max_decrease)

    max_increase_month = datetime.strftime(date_obj[max_increase_index + 1], "%b-%y") # + timedelta(days=max_increase_index), "%b-%y")
    max_decrease_month = datetime.strftime(date_obj[max_decrease_index + 1], "%b-%y") # + timedelta(days=max_decrease_index), "%b-%y")

    output_file.write(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")

# Print the results to the console
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Loss: ${total_pl}")
print(f"Average Change: ${average_monthly_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")

# Print a message indicating that the results have been saved to the text file
print("Financial analysis results have been saved to 'Financial_Analysis.txt'.")
