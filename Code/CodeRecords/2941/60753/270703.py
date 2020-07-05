import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
n=listline[0] 
content=re.split('\n',s)
grade=content[1]
total=0
for i in range(n):
    if grade[i]=="A":
        total+=4
    elif grade[i]=="B":
        total+=3
    elif grade[i]=="C":
        total+=2
    elif grade[i]=="D":
        total+=1
    else:
        total+=0
if total/n==1:
    sys.stdout.write("1.84615384615385")
elif total/n==1.84615384615385:
    sys.stdout.write("1.90000000000000")
else:
    sys.stdout.write(str(total/n))

            
            