import heapq
T=int(input())
for tt in range(T):
    n=int(input())
    for i in range(n):
        tmp=i*3+3
        if(tmp>n):
            print(-1)
            break
        if(tmp==n):
            print(i,i+1,i+2)
            break