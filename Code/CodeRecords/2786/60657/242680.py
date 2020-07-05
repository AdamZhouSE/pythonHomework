import re
up=input()
up=int(up)
arr=input().split(' ')

arr=[int(x) for x in arr]
arr.sort()
cons=0
temp=arr.copy()
mark=0
for i in range(1,len(arr)+1):
    mark = 0
    for k in range(len(temp)):
        if temp[k]!=0:
            if temp[k]>=i:
                temp[k]=0
                mark = 1
                break
            else:
                temp[k]=0
    if mark==1:
        cons+=1
print(cons)