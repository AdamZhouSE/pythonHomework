t=eval(input())
for _ in range(t):
    n=eval(input())
    arr=list(map(int,input().strip().split(' ')))
    maxD=0
    for i in range(n-1):
        for j in range(i+1,n):
            maxD=max(arr[j]-arr[i],maxD)
    if maxD!=0:
        print(maxD)
    else:
        print(-1)