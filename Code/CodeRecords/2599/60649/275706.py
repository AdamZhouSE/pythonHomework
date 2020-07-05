import heapq
heap=[]
N,M=map(int,input().split())
sum=[0 for i in range(100010)]
c=sum.copy()
a=[11111111111 for i in range(100010)]
a=[0]+a
b=a.copy()
for i in range(1,N+1):
    c[i]=int(input())
for i in range(1,M+1):
    a[i],b[i]=map(int,input().split())
a[M+1]=N+1
z=zip(a,b)
z=sorted(z)
t=0
ans=0
for i in range(1,N+1):
    while z[t+1][0]<=i:
        t+=1
        n=z[t][1]
        heapq.heappush(heap,-n)
        sum[n]+=1
    while len(heap)>c[i]+ans:
        x=heapq.heappop(heap)
        sum[-x]-=1
    ans+=sum[i]
print(ans)

