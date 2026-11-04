"""
RECORD CHECK  -  my version
===========================

Name  :  Yovan Prakash Cahoolessur
Lane  :  AI/DATA SCIENCE
Date  :  29/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

data_set =input("Enter Data set name : ") 
rows_loaded =float(input("Enter rows loaded : "))    #converts the input into float datatype
rows_expected =float(input("Enter rows expected : "))    

difference = rows_expected-rows_loaded     
percent = (rows_loaded/rows_expected)*100      

print("=" * 34) #Creates a header
print(f"  RECORD CHECK  -  {data_set}")
print("=" * 34)

print(f'Rows loaded        : {rows_loaded:>10.2f}\n'   #Output has been formatted to be right aligned(10) and to 2 decimal places
      f'Rows Expected      : {rows_expected:>10.2f} \n'
      f'Difference         : {difference:>+10.2f} \n'
      f'Percentage filled  : {percent:>10.2f} % \n'
      f'Percentage Unused  : {100-percent:>10.2f} %'    #Shows unused percentage
)
print("=" * 34)   

