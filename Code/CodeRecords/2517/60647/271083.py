e=[]
a=input().split(',')
e.append(a)
b=input().split(',')
e.append(b)
c=input().split(',')
e.append(c)
d=input().split(',')
e.append(d)
res=0
temp=[]
for i in range(len(a)):
    temp.append(i)
    temp.append(i)
    temp.append(i)
    temp.append(i)
from itertools import combinations
list=[]
for i in combinations(temp,4):
    list1=[]
    for j in i:
        list1.append(j)
    list.append(list1)
list2=[]
for i in list:
    if i not in list2:
        list2.append(i)
from itertools import permutations
for i in list2:
    templist=[]
    for j in permutations(i,4):
        list3=[]
        for k in j:
            list3.append(k)
        if list3 not in templist:
            templist.append(list3)
    for m in range(len(templist)):
        result=0
        for n in range(4):
            result+=int(e[n][int(templist[m][n])])
        if result==0:
            res+=1
print(res