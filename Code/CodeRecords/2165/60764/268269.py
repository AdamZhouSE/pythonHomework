def bfs(m,path):
    ind=0
    while ind<len(path):
        i=1
        while i<len(m):
            if m[i][0]==path[ind]:
                break
            i+=1
        j=1
        while j<len(m):
            if m[i][j]=='1' and m[0][j-1] not in path:
                path.append(m[0][j-1])
            j+=1
        ind+=1
T=int(input())
for t in range(T):
    n,start=input().split()
    n=int(n)
    m=[]
    for i in range(n+1):
        m.append(input().split())
    path=[start]
    bfs(m,path)
    print(" ".join(i for i in path))