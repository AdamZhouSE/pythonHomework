import queue
info=input().split()
n=int(info[0])
root=int(info[1])
lc=[0 for i in range(n+root)]
rc=[0 for i in range(n+root)]
def printbylevel(r):
    q=queue.Queue()
    q.put(r)
    level=1
    while q.qsize()!=0:
        tar = []
        l=q.qsize()
        print('Level', level, ':', end=' ')
        for i in range(l):
            curr=q.get()
            tar.append(curr)
            if lc[curr]!=0:
                q.put(lc[curr])
            if rc[curr]!=0:
                q.put(rc[curr])
        print(*tar)
        level+=1
def printbyzigzag(r):
    q = queue.Queue()
    q.put(r)
    level = 1
    while q.qsize() != 0:
        tar = []
        l = q.qsize()
        if level%2==1:
            label='from left to right: '
        else:
            label='from right to left: '
        print('Level',level,label,end='')
        for i in range(l):
            curr = q.get()
            tar.append(curr)
            if lc[curr] != 0:
                q.put(lc[curr])
            if rc[curr] != 0:
                q.put(rc[curr])
        if level%2==0:
            tar=reversed(tar)
        print(*tar)
        level += 1
for i in range(n):
    info=input().split()
    fa=int(info[0])
    lch=int(info[1])
    rch=int(info[2])
    lc[fa]=lch
    rc[fa]=rch
printbylevel(root)
printbyzigzag(root)
