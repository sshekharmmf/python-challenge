import os
import csv
election_csv = os.path.join( "PyPoll", "election_data.csv")
pyPoll_output = os.path.join("PyPoll", "election_output.txt")
with open(election_csv, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next( csvfile)
    #print("Header:{}.format(csv_header)")
    total_votes=0
    candidate=set()
    vote1=0
    vote2=0
    vote3=0
    vote4=0
    winner=0
    
    for row in csvreader:
        total_votes=total_votes+1
        #Candidate.add(row[2]) will print distinct candidate
        candidate.add(row[2])
        if row[2]== 'Correy':
            vote1=vote1+1
        elif row[2]=='Khan':
            vote2=vote2+1
        elif row[2]=='Li':
            vote3=vote3+1
        elif row[2]=="O'Tooley":
            vote4=vote4+1
        if max(vote1,vote2,vote3,vote4)==vote1:
            winner='Correy'
        elif max(vote1,vote2,vote3,vote4)==vote2:
            winner='Khan'
        elif max(vote1,vote2,vote3,vote4)==vote3:
            winner='Li'
        elif max(vote1,vote2,vote3,vote4)==vote4:
            winner=="O'Tooley"
               
        
    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")     
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    print("Khan: " + " " + str(round(((vote2/total_votes)*100)),) + "%" + " (" + str(vote2) + ")") 
    print("Correy: " + " " + str(round(((vote1/total_votes)*100)),) + "%" + " (" + str(vote1) + ")") 
    print("Li: " + " " + str(round(((vote3/total_votes)*100)),) + "%" + " (" + str(vote3) + ")")
    print("O'Tooley: " + " " + str(round(((vote4/total_votes)*100)),) + "%" + " (" + str(vote4) + ")")
    print("-------------------------")
   # print("Average Change: " + "$" + str(round(sum(rev_change) / len(rev_change),2)))
    #print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
   # print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    print("Winner: " + str(winner))
    print("-------------------------")
        
    # Output Files
with open(pyPoll_output, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(("Total Votes: " + str(total_votes)))
    txt_file.write("\n")
    txt_file.write(("Khan: " + " " + str(round(((vote2/total_votes)*100)),) + "%" + " (" + str(vote2) + ")") )
    txt_file.write("\n")
    txt_file.write(("Correy: " + " " + str(round(((vote1/total_votes)*100)),) + "%" + " (" + str(vote1) + ")"))
    txt_file.write("\n")
    txt_file.write(("Li: " + " " + str(round(((vote3/total_votes)*100)),) + "%" + " (" + str(vote3) + ")"))
    txt_file.write("\n")
    txt_file.write(("O'Tooley: " + " " + str(round(((vote4/total_votes)*100)),) + "%" + " (" + str(vote4) + ")"))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(("Winner: " + str(winner)))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    
    
        
        
            
            
        
    #print(vote4/total_votes)
        
    #print(candidate)
    #print(total_votes)
        
        

        