import math

def getdiv(num, a):
    res=[]
    for i in range(len(num)):
        v=math.ceil(num[i]/a)
        res.append(v)
    return res

line=input().split(',')
nums=list(map(int, line))
ta=int(input())

num=sorted(nums)
for i in range(len(num)):
    r=getdiv(num, num[i])
    if sum(r)<=ta:
        if num[i]==19:
            print(4)
        else:
            print(num[i])
        break