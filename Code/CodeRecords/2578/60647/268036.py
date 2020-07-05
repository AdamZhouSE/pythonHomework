list=input().split(",")
n=int(input())
import math
result=[]
for i in range(1,int(list[len(list)-1])+1):
    res=0
    for j in range(len(list)):
        res+=math.ceil(int(list[j])/i)
    if res<=n:
        print(i)
        break