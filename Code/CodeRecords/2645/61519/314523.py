import math
num=list(input().split(","))
num[0]=num[0][1:len(num[0])]
num[-1]=num[-1][0:-1]
for i in range(len(num)):
    num[i]=int(num[i])
d=int(input())
maxn=max(num)
res=[]
for i in range(1,maxn):
    tem=0
    for j in range(len(num)):
        tem=tem+math.ceil(num[j]/i)
    if tem==d:
        print(i)
        break