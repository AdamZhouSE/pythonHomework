def union(a,b):
    global f
    if getf(a)!=getf(b):
        f[getf(a)]=getf(b)
    return

def getf(x):
    global f
    while f[x]!=-1:
        x=f[x]
    return x

n=int(input())
connections=eval(input())
f=[-1 for i in range(0,n)]
if len(connections)<n-1:
    print(-1)
else:
    for connection in connections:
        union(connection[0],connection[1])
    num=0
    for i in f:
        if i==-1:
            num+=1
    print(num-1)