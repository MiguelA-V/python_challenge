#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:35:50 2020

@author: miguelvelez
"""

import pandas as pd
movie_file= '/Users/miguelvelez/Desktop/PyBank.csv'
 # Read and display the CSV with Pandas
data_df= pd.read_csv(movie_file)
data_df.head(10)
data_df.describe()

#number of months
Total_Months= len(data_df)
print(Total_Months)
    
total_profit= data_df["Profit/Losses"].sum()

print(total_profit)

net_total= '${:}'.format(total_profit)
print(net_total)

Profit_Loss= data_df["Profit/Losses"].values
print(Profit_Loss)
profit= []
var = []
for x in Profit_Loss:
    profit.append(x)
for i in range(len(profit)-1):
    var.append(profit[i+1]-profit[i])
    
print(max(var))
print(min(var))

Average_Change= '$(:)'.format(var)

increase= max(var)
print(increase)
Greatest_increase= "${:}".format(increase)

inc_date= data_df[data_df["Profit/Losses"].values==1170593]
print(inc_date)

Great_inc_date = inc_date['Date']
print(Great_inc_date.to_string())

Greatest_inc_date= "Feb-2012"
p=var.index(increase)+1
print(p)

Decrease = min(var)
Greatest_decrease= '${:}'.format(Decrease)
Dec_Date= data_df[data_df["Profit/Losses"]==-1196225]
Great_Dec_date= Dec_Date["Date"]
print(Great_Dec_date)
print(Great_Dec_date.to_string())



print("-------------------------------------------")
print("Financial Analysis")
print("-------------------------------------------")
print("Total_Months: " + str(Total_Months))
print("Total_Profits: " + str(total_profit))
print("Average_Change: " + str(Average_Change))
print("Greatest_increase: " + str(Greatest_inc_date) + "($"+ str(Greatest_increase) +")")
print("Greatest_decrease: " + str("September 2013") + "($"+ str(Greatest_decrease) +")")
print("----------------------------------------------")

    

with open('financial_analysis.txt','w') as text:
    text.write("-------------------------------------------")
    text.write("Financial Analysis")
    text.write("-------------------------------------------")
    text.write("Total_Months: " + str(Total_Months))
    text.write("Total_Profits: " + str(total_profit))
    text.write("Average_Change: " + str(Average_Change))
    text.write("Greatest_increase: " + str(Greatest_inc_date) + "($"+ str(Greatest_increase) +")")
    text.write("Greatest_decrease: " + str("September 2013") + "($"+ str(Greatest_decrease) +")")
    text.write("----------------------------------------------")
    










    







    
        







      
      






    
    
    
    
    









    




