"""
RECORD CHECK  -  my version
===========================

Name  : Yovan Prakash Cahoolessur
Lane  :  AI 
Date  :  06/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
def parse_line(raw_line):
    """Converts raw data into a structured dictionary"""
    line=raw_line.strip()
    survey_part,rest=line.split(",",1) 
    survey=survey_part.strip().lower()     #Cleans string and append to dictionary
    record={"survey":survey}
    for piece in rest.split(","):
        key,value=piece.split("=")
        record[key.strip().lower()]=float(value.strip()) 
    return record

def status_of(record):
    """Classify surveys based on rating"""
    rating=record["rating"]
    if rating<=2:
        return "FLAGGED"     #sets status based of rating
    else:
        return "OK"


raw_records = [] #creates a empty list

with open("tempmessy.txt") as f: #opens file in reading mode
    for line in f:
        if line.strip(): #ignores empty line in fine
            raw_records.append(line) #appends line into list

tot_records=0
flagged=0
print()
print()
for raw_record in raw_records:
    record=parse_line(raw_record)
    status=status_of(record)#fetch status
    print(f"{record}  :  {status}")

    tot_records+=1
    if status=="FLAGGED":
        flagged+=1

print()
print()
print(f"Summary : {tot_records} records \n"
      f"Flagged : {flagged} records")

print()
print()

try:
    parse_line("Survey_2222, rating=abc,age=def") 
except ValueError as err:  #test for valueerror
    print("Error : ",err)

    
print()
print()
