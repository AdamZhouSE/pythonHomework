import heapq
T=int(input())
for tt in range(T):
    n=int(input())-1
    a=list(map(int,input().split()))
    a.sort()
    if(n%2==1):
        print((a[n//2]+a[n//2+1])//2)
    else:
        print(a[n//2])