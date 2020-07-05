import sys
import re
import math
s=sys.stdin.read()
seats=s.split("\n")
n=int(seats[0])
del(seats[0])
oriseat=seats[0].split(" ")
finseat=seats[1].split(" ")
count=0
for i in range(n):
    teacher=oriseat[i]
    pos=0
    for j in range(n):
        if finseat[j]==teacher:
            break
        pos+=1
    for j in range(i):
        teacher2=oriseat[j]
        isSatisfied=1
        for k in range(pos,n):
            if finseat[k]==teacher2:
                isSatisfied=0
                break
        if isSatisfied==0:
            count+=1
print(count)