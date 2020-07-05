import math
cases=int(input())
for i in range(cases):
    n=int(input())
    nums=list(map(int,input().split()))
    a,b=min(nums),max(nums)
    print(a*b//math.gcd(a,b))