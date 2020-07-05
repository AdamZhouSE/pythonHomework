import math

n = int(input())
for j in range(n):
    n,l,r=map(int,input().split())
    Max=int(math.log(n,2))+1
    print(n|int((math.pow(2,min(r,Max))-math.pow(2,l-1))))