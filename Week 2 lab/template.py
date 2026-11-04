"""
RECORD CHECK  -  my version
===========================

Name  : Yovan Prakash Cahoolessur
Lane  :  AI 
Date  :03/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
count=0
while True:
    data_set =input("Enter Data set name : ") 
    if data_set=="quit": #condition to end loop
        break
    rows_loaded = float(input("Enter amount of rows loaded : "))
    rows_expected = float(input("Enter amount of rows expected : "))   #data entry
    difference = rows_expected-rows_loaded
    percent = (rows_loaded/rows_expected)*100     #calculats difference and percent from value and limit
    if percent>100:                 
        status="OVER LIMIT"    #deduces status
        count+=1
    elif percent>=90:
        status="WARNING"
    else:
        status="OK"
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {data_set}")
    print("=" * 34)

    print(f'Rows loaded     : {rows_loaded:>10.2f}\n'
          f'Rows Expected   : {rows_expected:>10.2f} \n'
          f'Difference      : {difference:>+10.2f} \n'
          f'Percentage      : {percent:>10.2f} % \n'
          f'Status          : {status:>10}'
    )
    print("=" * 34)
print(f"Amount of OVER LIMIT : {count}")
