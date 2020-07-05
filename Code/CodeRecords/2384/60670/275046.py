t=int(input())
for k in range(0,t):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(1,n+2):
        if not(i in arr):
            print(i)
            break