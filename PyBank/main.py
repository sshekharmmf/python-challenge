import os
import csv

budget_csv = os.path.join( "PyBank", "budget_data.csv")
pyBank_text = os.path.join("PyBank", "budget_output.txt")
# Read the file
with open(budget_csv, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next( csvfile)
    #print("Header:{}.format(csv_header)")
    total_months=0
    total_profit=0
    prev_profit=0
    profit_change=0
    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999999]
    
    rev_change=[]
    for row in csvreader:
        total_months=total_months+1
        total_profit=total_profit+int(row[1])
        profit_change= int(row[1])-prev_profit
        prev_profit=int(row[1])
        if(profit_change==int(row[1])):
             profit_change=0
        rev_change.append(int(profit_change))
        try:
            rev_change.remove(0)
         
        except ValueError: 
            pass
        
        #rev_change.append(int(row[1]))
                
        if(profit_change > greatest_increase[1]):
            greatest_increase[1]= profit_change
            greatest_increase[0]=row[0]
        
        if(profit_change < greatest_decrease[1]):
            greatest_decrease[1]= profit_change
            greatest_decrease[0]=row[0]
        
        
        
    #print(profit_change)
      
        
    revenue_avg = sum(rev_change) / len(rev_change)
                
   
        
    #rev_avg=sum(rev_change)/len(rev_change)
        

      
        #rev_change.append(row[2])
    
        #total_profit.append(row[1])
        #total_revenue=sum((total_profit))
        #total1=list(str(total_months))
        #total2=len(total1)
    #print("Total Months: " + str(total_months))
    #print("Total profit/loss:"+ str(total_profit))
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(round(sum(rev_change) / len(rev_change),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
        
       
  # Output Files
with open(pyBank_text, "w") as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_profit))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(rev_change) / len(rev_change),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

