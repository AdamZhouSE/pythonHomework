import heapq
T=int(input())
for tt in range(T):
    n=int(input())
    ans=0
    for i in n:
        if(i**2==n):
            ans=1
            break
    print(ans)