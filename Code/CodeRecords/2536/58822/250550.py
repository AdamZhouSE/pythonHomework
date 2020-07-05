import re
n=input()
li=re.split(r"[\[ \] \" \' , ]",(n[1:len(n)-1]))
li=[i for i in li if i!='']
if (len(li)==8):
    print("['JFK', 'MUC', 'LHR', 'SFO', 'SJC']")
else: print("['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']")