"""
RECORD CHECK  -  my version
===========================

Name  : Yovan Prakash Cahoolessur
Lane  :  AI      (delete two)
Date  :03/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

# data_set =input("Enter Data set name : ")      
# rows_loaded = float(input("Enter amount of rows loaded : "))     
# rows_expected = float(input("Enter amount of rows expected : "))  


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

# difference = rows_expected-rows_loaded  
# percent = (rows_loaded/rows_expected)*100  
# ====================================================================     
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

# if percent>100:                 
#     status="OVER LIMIT"
# elif percent>=90:
#     status="WARNING"
# else:
#     status="OK"


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

count=0
while True:
    data_set =input("Enter Data set name : ") 
    if data_set=="quit":
        break
    rows_loaded = float(input("Enter amount of rows loaded : "))
    rows_expected = float(input("Enter amount of rows expected : "))
    difference = rows_expected-rows_loaded
    percent = (rows_loaded/rows_expected)*100
    if percent>100:                 
        status="OVER LIMIT"
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
# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
