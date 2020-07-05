import math

n = int(input())
for j in range(n):
    n,l,r=map(int,input().split())
    print(int(n+math.pow(2,r)-math.pow(2,l-1)))
    ans=n+math.pow(2,r)-math.pow(2,l-1)
    if ans==23:
        print(n,l,r)