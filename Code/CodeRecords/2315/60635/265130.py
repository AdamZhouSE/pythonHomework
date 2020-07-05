import queue
n=int(input())
lc=[-1 for i in range(n)]
rc=[-1 for i in range(n)]
for i in range(n-1):
    info=input().split()
    fa=int(info[0])
    c=int(info[1])
    if lc[fa]<0:
        lc[fa]=c
    else:
        rc[fa]=c
def countlevel(r):
    q=queue.Queue()
    q.put(r)
    level=0
    while q.qsize()!=0:
        l=q.qsize()
        for i in range(l):
            curr=q.get()
            if lc[curr]>=0:
                q.put(lc[curr])
            if rc[curr]>=0:
                q.put(rc[curr])
        level+=1
    return level
print(countlevel(0))
