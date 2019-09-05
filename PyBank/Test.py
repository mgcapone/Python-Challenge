import os
import csv

#Path to collect the data 
budget_data = os.path.join("..", "PyBank", "budget_data.csv")

with open('budget_data.csv', newline='') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')
    header = next(csvreader)
    
    months=0
    net_profits = 0
    monthly_change = 0
    previous_month_profit = 0
    max_change = 0
    min_change = 0
      
    #Read each row of data after the header
    for row in csvreader:
        #print(row)
        profits = row[1]
        #print(profits)
        months += 1
        net_profits = 0
        min_date = row[0]
        max_date = row[0]
        monthly_change = 0
        total_changes = 0
        max_change = 0
        min_change = 0 
        
        if months == 1:
           monthly_change = 0
           previous_month_profit = profits
           total_changes = total_changes + monthly_change
           net_profits = float(profits) +  net_profits    
        else:
           monthly_change = float(profits) - float(previous_month_profit) 
           previous_month_profit = profits
           total_changes = total_changes + monthly_change
           net_profits = float(profits) +  net_profits
           conversion = '${:,.2f}'.format(monthly_change)
           print(conversion)
           
        if monthly_change > max_change:
            max_change = monthly_change
            max_date = row[0]
   
average = total_changes/(months - 1)            
  
#print(net_profits) 
#print(months)  
print(max_date)
#print(max_change)
#print(average)
#print(total_changes)       