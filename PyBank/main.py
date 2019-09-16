{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 225,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 230,
   "metadata": {},
   "outputs": [],
   "source": [
    "budget_csv = os.path.join( \"PyBank\", \"budget_data.csv\")\n",
    "pyBank_text = os.path.join(\"PyBank\", \"budget_output.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 231,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'PyBank\\\\budget_data.csv'"
      ]
     },
     "execution_count": 231,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "budget_csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 269,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "\n",
      "Financial Analysis\n",
      "-------------------------\n",
      "Total Months: 86\n",
      "Total Revenue: $38382578\n",
      "Average Change: $-2315.12\n",
      "Greatest Increase: Feb-12 ($1926159)\n",
      "Greatest Decrease: Sep-13 ($-2196167)\n"
     ]
    }
   ],
   "source": [
    "# Read the file\n",
    "with open(budget_csv, newline=\"\") as csvfile:\n",
    "    csvreader=csv.reader(csvfile,delimiter=\",\")\n",
    "    csv_header=next( csvfile)\n",
    "    #print(\"Header:{}.format(csv_header)\")\n",
    "    total_months=0\n",
    "    total_profit=0\n",
    "    prev_profit=0\n",
    "    profit_change=0\n",
    "    greatest_increase = [\"\", 0]\n",
    "    greatest_decrease = [\"\", 9999999999999999]\n",
    "    \n",
    "    rev_change=[]\n",
    "    for row in csvreader:\n",
    "        total_months=total_months+1\n",
    "        total_profit=total_profit+int(row[1])\n",
    "        profit_change= int(row[1])-prev_profit\n",
    "        prev_profit=int(row[1])\n",
    "        if(profit_change==int(row[1])):\n",
    "             profit_change=0\n",
    "        rev_change.append(int(profit_change))\n",
    "        try:\n",
    "            rev_change.remove(0)\n",
    "         \n",
    "        except ValueError: \n",
    "            pass\n",
    "        \n",
    "        #rev_change.append(int(row[1]))\n",
    "                \n",
    "        if(profit_change > greatest_increase[1]):\n",
    "            greatest_increase[1]= profit_change\n",
    "            greatest_increase[0]=row[0]\n",
    "        \n",
    "        if(profit_change < greatest_decrease[1]):\n",
    "            greatest_decrease[1]= profit_change\n",
    "            greatest_decrease[0]=row[0]\n",
    "        \n",
    "        \n",
    "        \n",
    "    #print(profit_change)\n",
    "      \n",
    "        \n",
    "    revenue_avg = sum(rev_change) / len(rev_change)\n",
    "                \n",
    "   \n",
    "        \n",
    "    #rev_avg=sum(rev_change)/len(rev_change)\n",
    "        \n",
    "\n",
    "      \n",
    "        #rev_change.append(row[2])\n",
    "    \n",
    "        #total_profit.append(row[1])\n",
    "        #total_revenue=sum((total_profit))\n",
    "        #total1=list(str(total_months))\n",
    "        #total2=len(total1)\n",
    "    #print(\"Total Months: \" + str(total_months))\n",
    "    #print(\"Total profit/loss:\"+ str(total_profit))\n",
    "    print()\n",
    "    print()\n",
    "    print()\n",
    "    print(\"Financial Analysis\")\n",
    "    print(\"-------------------------\")\n",
    "    print(\"Total Months: \" + str(total_months))\n",
    "    print(\"Total Revenue: \" + \"$\" + str(total_profit))\n",
    "    print(\"Average Change: \" + \"$\" + str(round(sum(rev_change) / len(rev_change),2)))\n",
    "    print(\"Greatest Increase: \" + str(greatest_increase[0]) + \" ($\" +  str(greatest_increase[1]) + \")\") \n",
    "    print(\"Greatest Decrease: \" + str(greatest_decrease[0]) + \" ($\" +  str(greatest_decrease[1]) + \")\")\n",
    "        \n",
    "       \n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 270,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Output Files\n",
    "with open(pyBank_text, \"w\") as txt_file:\n",
    "    txt_file.write(\"Financial Analysis\")\n",
    "    txt_file.write(\"\\n\")\n",
    "    txt_file.write(\"-------------------------\")\n",
    "    txt_file.write(\"Total Months: \" + str(total_months))\n",
    "    txt_file.write(\"\\n\")\n",
    "    txt_file.write(\"Total Revenue: \" + \"$\" + str(total_profit))\n",
    "    txt_file.write(\"\\n\")\n",
    "    txt_file.write(\"Average Change: \" + \"$\" + str(round(sum(rev_change) / len(rev_change),2)))\n",
    "    txt_file.write(\"\\n\")\n",
    "    txt_file.write(\"Greatest Increase: \" + str(greatest_increase[0]) + \" ($\" + str(greatest_increase[1]) + \")\") \n",
    "    txt_file.write(\"\\n\")\n",
    "    txt_file.write(\"Greatest Decrease: \" + str(greatest_decrease[0]) + \" ($\" + str(greatest_decrease[1]) + \")\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 272,
   "metadata": {},
   "outputs": [],
   "source": [
    "#(rev_change)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 271,
   "metadata": {},
   "outputs": [],
   "source": [
    "#sum(rev_change)/len(rev_change)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
