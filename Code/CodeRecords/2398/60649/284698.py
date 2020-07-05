import queue
def check(x):
    f=0
    q=queue.PriorityQueue()
    for i in range(1,x+1):
        q.put(d[i],d[i])
    if f>t:
        return 0
    z,c=x+1,0
    for i in range(z,n+1):
        tmp=q.get()
        f=f+tmp-c
        c=tmp
        if f>t:
            return 0
        q.put(d[i]+c,d[i]+c)
    for i in range(1,x+1):
        tmp=q.get()
        f=f+tmp-c
        c=tmp
        if f>t:
            return 0
    return 1
n,t=map(int,input().split())
d=[0 for i in range(n+1)]
for i in range(1,n+1):
    d[i]=int(input())
l,r=1,n
try:
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            r = mid - 1
        else:
            l = mid + 1
except:
    print(d,t)
print(l)