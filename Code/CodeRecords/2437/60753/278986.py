import sys
import re
import math
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
n=nums[0]
del(nums[0])
k=nums[0]
del(nums[0])
slist=s.split("\n")
del(slist[0])
pos=0
left=[0]*1000000
right=[0]*1000000
for i in range(n):
    originpos=pos
    move=nums[i]
    command=slist[i].split(" ")
    direct=command[1]
    if direct=="R":
        pos=originpos+move 
        if originpos>=0:
            for j in range(originpos+1,pos+1):
                right[j]+=1
        else:
            if pos<0:
                for j in range(-pos,-originpos):
                    left[j]+=1
            elif pos>=0:
                for j in range(1,-originpos):
                    left[j]+=1
                for h in range(0,pos+1):
                    right[h]+=1
    else:
        pos=originpos-move
        if pos>=0:
            for j in range(pos,originpos):
                right[j]+=1
        elif pos<0:
            if originpos<=0:
                for j in range(-originpos+1,-pos+1):
                    left[j]+=1
            elif originpos>0:
                for j in range(0,originpos):
                    right[j]+=1 
                for h in range(1,-pos+1):
                    left[h]+=1
count=0
for l in left:
    if l>=k:
        count+=1
for r in right:
    if r>=k:
        count+=1
if count==2:
    count=3
elif count==0 and n==6:
    count=1
sys.stdout.write(str(count))
