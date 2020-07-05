import math

n = int(input())
for j in range(n):
    n,l,r=map(int,input().split())
    print(n+math.pow(2,l-1)+math.pow(2,r-1))