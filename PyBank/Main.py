import os
import csv

BankCSV = os.path.join('..','PyBank','budget_data.csv')
output_path = os.path.join('..','PyBank','FinancialAnalysis.csv',)

# Calculate total months
with open(BankCSV,'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    next(csvfile)
    MonthData = list(reader)
    Months = len(MonthData)
    #print(Months)
    

# Calculate aggregate P/L
with open(BankCSV,'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    next(csvfile)
    TotalPL = 0
    for row in csv.reader(csvfile):
        TotalPL += float(row[1])
        MoneyConversion = '${:,.2f}'.format(TotalPL)
    #print(MoneyConversion)


# Monthly PL change
with open(BankCSV,'r') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    next(csvfile)
    reader = csv.reader(csvfile)
    flatfile = []
    for row in reader:
        flatfile.append(row)

MonthlyChange = []
for ix, row in enumerate(flatfile):
    if ix == 0:
        continue
    else:
        MonthlyChange.append(float(row[1]) - float(flatfile[ix-1][1]))

maxprofit = max(MonthlyChange)
maxprofitconverted = '${:,.2f}'.format(maxprofit)
maxloss = min(MonthlyChange)
maxlossconverted = '${:,.2f}'.format(maxloss)
averagechange = sum(MonthlyChange)/len(MonthlyChange)
averagechangeconverted = '${:,.2f}'.format(averagechange)

print('Financial Analysis')
print('---------------------------')
print('Total Months: ' + str(Months))
print('Total: ' + str(MoneyConversion))
print('Average Change: ' + str(averagechangeconverted))
print('Greatest Increase in Profits: ' + str(maxprofitconverted))
print('Greatest Decrease in Profits: ' + str(maxlossconverted))

with open(output_path, 'w', newline=' ') as csvfile:

    csvwriter = csv.writer(csvfile, delimimter=',')

