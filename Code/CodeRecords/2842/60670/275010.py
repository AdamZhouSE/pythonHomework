def search(i,depth):
    global visited,f,maxn
    if i==-1:
        if depth>maxn:
            maxn=depth
        return
    search(f[i],depth+1)

n=int(input())
f=[]
for i in range(0,n):
    f.append(int(input()))
visited=[False for i in range(0,n)]
maxn=0
for i in range(0,n):
    if !visited[i]:
        search(i,0)
print(maxn)