import queue
n,m=map(int,input().split())
q=queue.LifoQueue()
a=[1 for i in range(n+1)]
a[0]=0
for _ in range(m):
    s=input().split()
    if s[0]=='R':
        if q.qsize()>0:
            t=q.get()
            a[t]=1
    else:
        x=int(s[1])
        if s[0]=='D':
            a[x]=0
            q.put(x)
        else:
            res=1
            if a[x]==0:
                res=0
            else:
                left,right=x-1,x+1
                while left>0 and a[left]==1:
                    left-=1
                    res+=1
                while right<=n and a[right]==1:
                    right+=1
                    res+=1
            print(res)
