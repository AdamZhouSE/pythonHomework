import sys
import re
s=sys.stdin.read()
digits=re.findall(r"\d+",s)
listline= [int(e) for e in digits ]
if len(listline)<=1:
    print("False")
elif len(listline)==2:
    if listline[0]==listline[1]:
        print("True")
    else:
        print("False")
else:
    count=[0]*10000
    filter=list(set(listline))
    for i in range(len(listline)):
        count[listline[i]-1]+=1
    isvalid=1
    for i in range(len(filter)-1):
        if count[filter[i]-1]!=count[filter[i+1]-1]:
            if count[filter[i]-1]%count[filter[i+1]-1]!=0 and count[filter[i+1]-1]%count[filter[i]-1]!=0:
                isvalid=0
                break
    if isvalid==1:
        print("True")
    else:
        print("False")
