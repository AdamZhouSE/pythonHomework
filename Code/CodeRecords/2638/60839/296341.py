import math
import re

def average(lis):
    ave=0
    for i in lis:
        ave+=i
    ave=ave/len(lis)
    return ave
def fangcha(lis):
    ave=average(lis)
    fang=0
    for i in lis:
        fang+=math.pow(i-ave,2)
    return fang/len(lis)

lis=list(map(int,input().split(" ")))
n=lis[0]
m=lis[1]
num=list(map(int,input().split(" ")))
ans=[]
for i in range(0,m):
    lis1=list(map(int,input().split(" ")))
    if lis1[0]==1:
        for j in range(lis1[1]-1,lis1[2]):
            a=lis1[3]
            num[j]+=a
    elif lis1[0]==2:
        lis2=[]
        for k in range(lis1[1]-1,lis1[2]):
            lis2.append(num[k])
        ans.append(format(average(lis2),'0.4f'))
    elif lis1[0]==3:
        lis2 = []
        for k in range(lis1[1] - 1, lis1[2]):
            lis2.append(num[k])
        ans.append((format(fangcha(lis2),'0.4f')))
for i in ans:
    print(i)