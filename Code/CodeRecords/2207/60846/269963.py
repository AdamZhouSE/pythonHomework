t=int(input())
while t:
    line=[int(x) for x in input().split()]
    n=line[0]
    k=line[1]
    sum=(1+k)*k//2
    if sum>n: print(0)
    else: print(1)
    t-=1