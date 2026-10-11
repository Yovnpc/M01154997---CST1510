"""
RECORD CHECK  -  my version
===========================

Name  :Yovan Prakash Cahoolessur
Lane  :  AI 
Date  :10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
def status_of(percent):
    """Returns a string depending on the the value of percent"""
    if percent>=100:
        return "OVER LIMIT"
    elif percent>=90:
        return "WARNING"
    else:
        return "OK"
    
def check(value,limit):
    """Returns the difference and percentage"""
    difference=limit-value
    percent=(value/limit)*100
    return difference,percent

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

label=""
overlimit=0

while label!="quit":
    label = input("Enter Data set name : ") 
    if label=="quit":
        break
    value = float(input("Enter rows loaded : "))   
    limit = float(input("Enter rows expected : ")) 
    difference,percent=check(value,limit)
    status = status_of(percent)
    print_report(value=value,label=label,limit=limit,difference=difference,percent=percent,status=status)
    if status=="OVER LIMIT":
        overlimit+=1

print(f'Amount of overlimit : {overlimit}')
