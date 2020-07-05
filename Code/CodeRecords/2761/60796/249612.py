import math
n=int(input())
result=[]
while n>0:
    N=int(input())
    total=1
    for i in range(1,N+1):
        total=math.pow(i,2)+total
    result.append(total)
    n=n-1

for i in range(len(result)):
    print(result[i])