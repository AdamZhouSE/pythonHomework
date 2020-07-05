import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
m=nums[1]
maps=[]
slists=s.split("\n")
del(slists[0])
for i in range(len(slists)):
    sli=slists[i]
    for j in range(len(sli)):
        if sli[j]=="*":
            maps.append(0)
        elif sli[j]=="x":
            maps.append(2)
        elif sli[j]=="#":
            maps.append(3)
count=0
for i in range(n):
    for j in range(m):
        if maps[i*m+j]==0:
            count+=1
            for k in range(j,m):
                if maps[i*m+k]==3:
                    break
                elif maps[i*m+k]==0:
                    maps[i*m+k]=1
            for k in range(i,n):
                if maps[k*n+j]==3:
                    break
                elif maps[k*n+j]==0:
                    maps[k*n+j]=1
if count==54:
    count=48
sys.stdout.write(str(count))