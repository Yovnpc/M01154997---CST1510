"""
RECORD CHECK  -  my version
===========================

Name  :  Yovan Prakash Cahoolessur
Lane  :  AI
Date  :  14/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
def check_record(value,limit):
    """Returns the difference, percentage and status"""
    difference=limit-value
    percent=(value/limit)*100
    status=""
    if percent>=100:
        status= "OVER LIMIT"
    elif percent>=90:
        status= "WARNING"
    else:
        status= "OK"
    return  difference,percent,status           #returns a tuple


def print_report(label,value,limit,difference,percent,status): 
    """Prints out the data"""
    print()
    print("="*34)
    print(f"  RECORD CHECK  -  {label}")
    print("="*34)
    print(f'Rows loaded   : {value:>10.2f}\n'
          f'Rows expected : {limit:>10.2f}\n'
          f'Free          : {difference:>10.2f}\n'
          f'Percentage    : {percent:>+10.2f}%\n'
          f'Status        : {status:>10}'
          )
    print("="*34)


def load_records(path):
    """Returns extracted data from file as a list """
    file_data=[]
    with open(path) as f:
        for line in f:
            ln=line.strip() #removes whitespace
            label,value,limit=ln.split(",") #Assigns data to their counterpart as a tuple
            value=float(value)
            limit=float(limit)
            difference,percent,status=check_record(value,limit) #calls check_record with value,limit,assigns return data to a tuple
            file_data.append({"label":label,"value":value,"limit":limit,"difference":difference,"percent":percent,"status":status})#adds data to dictionary
    return file_data #returns a dictionary



try:   #to check for errors
    records=load_records("temprecords.txt") #assigns file converted to dictionary to a variable
    overlimit=0
    with open("tempresults.txt","w+") as f: #open file in writing mode
        for line in records:
            label,value,limit,difference,percent,status = line["label"],line["value"],line["limit"],line["difference"],line["percent"],line["status"] #loads each data in the line of the dictionary into their respective variable
            print_report(value=value,limit=limit,label=label,difference=difference,percent=percent,status=status)
            if status=="OVER LIMIT": #checkes for overlimit status
                overlimit+=1 
            f.write(f"{label} {status}\n") #writes label and status to tempresults file
    with open("tempresults.txt") as results:   
        text=results.read()     #assigns tempresult file to a variable then prints
        print(text)    
except FileNotFoundError:
    print("File does not exist") #output incase of nonexistent file error
  

print(f'Overlimit = {overlimit}') #output how much data parcel are ovelimit
