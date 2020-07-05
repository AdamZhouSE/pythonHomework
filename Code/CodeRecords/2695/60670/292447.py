def doadd(x,a):
    global tree,edge
    tree[x]+=a
    for i in range(0,n):
        if edge[x][i]==1:
            doadd(i,a)
    return

def search(x):
    global tree,edge
    tmp=tree[x]
    for i in range(0,n):
        if edge[i][x]==1:
            tmp+=search(i)
    return tmp
        
n,m=map(int,input().split())
tree=list(map(int,input().split()))
edge=[[0 for i in range(0,n)] for i in range(0,n)]
for i in range(0,n-1):
    fr,to=map(int,input().split())
    edge[fr-1][to-1]=1
for i in range(0,m):
    op=list(map(int,input().split()))
    if op[0]==1:
        tree[op[1]-1]+=op[2]
    elif op[0]==2:
        doadd(op[1]-1,op[2])
    else:
        print(search(op[1]-1))