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
    return  difference,percent,status           


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
    """Reads file , """
    list=[]
    with open(path) as f:
        for line in f:
            ln=line.strip()
            label,value,limit=ln.split(",")
            value=float(value)
            limit=float(limit)
            difference,percent,status=check_record(value,limit)
            list.append({"label":label,"value":value,"limit":limit,"difference":difference,"percent":percent,"status":status})
    return list



try:
    records=load_records("temprecords.txt")
    overlimit=0
    with open("tempresults.txt","w+") as f:
        for line in records:
            label,value,limit,difference,percent,status = line["label"],line["value"],line["limit"],line["difference"],line["percent"],line["status"]
            print_report(value=value,limit=limit,label=label,difference=difference,percent=percent,status=status)
            if status=="OVER LIMIT":
                overlimit+=1
            f.write(f"{label} {status}\n")
    with open("tempresults.txt") as results:   
        text=results.read()     
        print(text)    
except FileNotFoundError:
    print("File does not exist")
  

print(f'Overlimit = {overlimit}')
