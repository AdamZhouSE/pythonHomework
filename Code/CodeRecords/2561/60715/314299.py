import operator

from functools import reduce
T=int(input())
while T>0:
    n,x=map(int,input().split())
    l=2*n
    t1=[]
    t2=[]
    count=0
    re=1
    while re<=2*n:
        num=[int(n) for n in input().split()]
        if re<=n:
            t1.append(num)
        else:
            t2.append(num)
        re+=1
    ma=reduce(operator.add, t1)
    mb=reduce(operator.add, t2)
    for i in range(len(ma)-1):
        for j in range(i+1,len(ma)):
            if ma[i]+ma[j]==x:
                count+=1
    for i in range(len(mb)-1):
        for j in range(i+1,len(mb)):
            if mb[i]+mb[j]==x:
                count+=1
    print(count)