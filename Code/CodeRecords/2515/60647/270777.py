list=input().split(",")
n=int(input())
all=[]
from itertools import combinations
# 0 0 0 0 0 0
res=[]
for i in range(len(list)-1):
    res.append(i)
list2=[]
for i in combinations(res,n-1):
    list2.append(i)
result=[]
for i in list2:
    temp=[]
    temp1=[]
    for j in i:
        temp.append(int(j))
    for j in range(len(temp)):
        restemp=0
        if j==0:
           for k in range(0,int(temp[0])+1):
               restemp += int(list[k])
           temp1.append(restemp)
        elif j==len(temp)-1:
            for k in range(temp[len(temp)-1]+1,len(list)):
                restemp+=int(list[k])
            temp1.append(restemp)
        else:
            for k in range(temp[j] + 1, temp[j + 1] + 1):
                restemp += int(list[k])
            temp1.append(restemp)
            restemp=0
            for k in range(temp[j - 1] + 1, temp[j] + 1):
                restemp += int(list[k])
            temp1.append(restemp)
    if len(temp)==2:
        restemp=0
        for k in range(temp[0] + 1, temp[1] + 1):
            restemp += int(list[k])
        temp1.append(restemp)
    if len(temp)==1:
        restemp=0
        for k in range(temp[0] + 1,len(list)):
            restemp += int(list[k])
        temp1.append(restemp)
    temp1.sort()
    if len(temp1)!=0:
        all.append(temp1[len(temp1)-1])
    else:
        c=0
        for i in list:
            c+=int(i)
        print(c)
         
all.sort()
print(all[0])