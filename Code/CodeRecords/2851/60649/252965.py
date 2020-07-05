import math
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
max1=0
for i in range(n):
    xi=l[i][0]
    yi=l[i][1]
    tmp=xi+yi
    max1=max(max1,tmp)
print(max1)