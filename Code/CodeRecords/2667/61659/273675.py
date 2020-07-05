import math
T=int(input())

for k in range(0,T):
    temp=list(input().split(" "))
    i=int(temp[0])
    n=int(temp[1])

    print(round(math.pow(2,n))-i)