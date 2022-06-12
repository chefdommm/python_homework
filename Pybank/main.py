#!/usr/bin/env python
# coding: utf-8

# In[13]:


from pathlib import Path
import csv


# In[14]:


csvpath = Path("C:/Users/chefd/OneDrive/Desktop/csv/budget_data.csv")


# In[17]:


total_number_months = 0
net_total = 0
profit_or_loss = 0
monthly_profit_loss = []
monthly_change = []


highest_profit_date = ""
highest_profit_value = 0
highest_loss_date = ""
highest_loss_value = 0


# In[19]:


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    
    
    for row in (csvreader):
        date = str(row[0])
        profit_or_loss = profit_or_loss + int(row[1])
        total_number_months = total_number_months + 1
        monthly_profit_loss.append(int(row[1]))
        
        
        if highest_profit_value == 0:
            highest_profit_value = int(row[1])
            highest_profit_date = date
            highest_loss_value = int(row[1])
            highest_loss_date = date
        elif int(row[1]) > highest_profit_value:
            highest_profit_value = int(row[1])
            highest_profit_date = date
        if int(row[1]) < highest_loss_value:
            highest_loss_value = int(row[1])
            highest_loss_date = date
            
            
            
    for i in range(len(monthly_profit_loss)-1):
        
        monthly_change.append(monthly_profit_loss[i+1]-monthly_profit_loss[i])
        increase_value = max(monthly_change)
        decrease_value = min(monthly_change)
        
    for pnl in monthly_change:
        net_total = net_total + pnl
        
    average_difference = round(net_total/len(monthly_change),2)


# In[25]:


print("Financial Analysis")
print("===============================================")
print("Total Months:", total_number_months)
print(f"Total ${profit_or_loss}")
print(f"The Average Change was: ${average_difference}")
print(f"The Greatest Increase in Profits: {highest_profit_date} ${increase_value}")
print(f"The Greatest Decrease in Profits: {highest_loss_date} ${decrease_value}")


# In[ ]:




