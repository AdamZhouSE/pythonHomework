t=int(input())
for i in range(t):
    n,x=list(map(int,input().strip().split()))
    if x<10:
        time=(10-x)*(n-1)
    else:
        time=0
    print(time)