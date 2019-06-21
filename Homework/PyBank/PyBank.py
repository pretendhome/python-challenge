import os
import csv



csvpath = os.path.join('/Users', 'neimical', 'Desktop', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    profit = csv.reader(csvfile, delimiter=',')
    print(profit)

    change = []

    csv_header = next(profit)
    print(f"CSV Header: {csv_header}")

    first_row = next(profit)

    prior = int(first_row[1])

    profit_loss = int(first_row[1])
    total_months = 1
    current = 0
    net_change = 0
    average_change = 0
    greatest_increase = 0
    smallest_increase = 0

    for row in profit:
        total_months = total_months + 1
        profit_loss = profit_loss + int(row[1])
        net_change = int(row[1]) - prior
        change.append(net_change)
        prior = int(row[1])

    greatest_increase = max(change)
    smallest_increase = min(change)
    average_change = sum(change) / len(change)

    print(f"Total Months: {total_months}")
    print(f"Total: {profit_loss}")
    print(f"Average change in Profits: {average_change}")
    print(f"Greatest Increase in Profits: {str(greatest_increase)}")
    print(f"Greatest Decrease in Profits: {str(smallest_increase)}")
