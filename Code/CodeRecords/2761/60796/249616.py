import math
n=int(input())
result=[]
while n>0:
    N=int(input())
    total=0
    for i in range(1,N+1):
        total=total+int(math.pow(i,2))
    result.append(total)
    n=n-1

for i in range(len(result)):
    print(result[i])