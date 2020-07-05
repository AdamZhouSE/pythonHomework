import math
N=int(input())
result=[]
ls=[1]
n=1
while len(ls)<N:
    m=pow(2,n)
    s=[max(ls)+1]
    if n%2==1:#从右到左
        while len(s)<m:
            s=[s[0]+1]+s
    else:#从左到右
        while len(s)<m:
            s.append(s[len(s)-1]+1)
    n=n+1
    ls=ls+s
i=0
while ls[i]!=N:
    i=i+1

while True:
    result=[ls[i]]+result
    if result[0]==1:
        break
    else:
        i = math.ceil((i - 2) / 2)

print(result)




