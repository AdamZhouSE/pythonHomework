import math


def com(k):
    sum=0
    for i in range(k+1):
        sum=sum+math.pow(i,5)
    return sum
n = int(input())
li_num=[]
a=0
r=0
for i in range(n):
    a=int(input())
    li_num.append(a)
    r=int(com(a))
    print(r)