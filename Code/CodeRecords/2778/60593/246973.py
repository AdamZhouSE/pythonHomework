import heapq
T=int(input())
for tt in range(T):
    l,r=map(int,input().split())
    ans=0
    for i in range(l,r+1):
        s=str(i)
        if(s[0]==s[len(s)-1]):
            ans+=1
    print(ans)