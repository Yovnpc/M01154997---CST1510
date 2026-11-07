"""
RECORD CHECK  -  my version
===========================

Name  : Yovan Prakash Cahoolessur
Lane  :  AI / Cyber / IT      (delete two)
Date  : 06/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("temp_records.csv")


#Calculate the percentage of rows loaded
df["percent"]=(df["rows_loaded"]/df["rows_expected"])*100 

#Creates column "status" based on the "percent"
df["status"]=df["percent"].apply(lambda p: "OVER LIMIT" if p>=100 else "WARNING" if p>=90 else "OK")

#Prints the full dataframe
print(df)

print()#spacing between prints
print()

#prints records that are not "OK"
print(df[df["status"]!="OK"])

print()
print()

#counts how much each "status" has occured
count_status=df.groupby("status").size() # df["status"].value_counts()
print(count_status)

#loads the whole dataframe into a new csv file
df.to_csv("temp_report.csv",index=False)


#create and save a bar chart of the status counts
count_status.plot(kind="bar",title="Status counter",xlabel="Status",ylabel="Occurence(count)")
plt.tight_layout() #makes the bar chart elements fit the png
plt.savefig("Count_Of_Status.png") #Saves the bar chart as a png
