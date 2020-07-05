def search(i,depth):
    print(i,depth)
    global visited,f,maxn
    if i==-1:
        if depth>maxn:
            maxn=depth
        return
    visited[i]=True
    search(f[i],depth+1)

n=int(input())
f=[]
for i in range(0,n):
    f.append(int(input()))
print(f)
visited=[False for i in range(0,n)]
maxn=0
for i in range(0,n):
    if visited[i]==False:
        search(i,0)
print(maxn)