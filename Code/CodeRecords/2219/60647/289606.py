n=int(input())
list=[]
from itertools import combinations
for i in range(n+1):
    list.append(i)
    list.append(i)
res=[]
for i in combinations(list,2):
    temp=[]
    for j in i:
        temp.append(j)
    if temp[0]*temp[0]+temp[1]*temp[1]==n:
        res.append(temp)
if len(res)!=0:
    print('True')
else:
    print(n)