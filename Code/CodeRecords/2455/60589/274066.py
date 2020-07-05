class node(object):
    def __init__(self,next,to):
        self.next=next
        self.to=to

def add(x,y):
    global cnt
    cnt+=1
    tree[cnt].next = head[x]
    tree[cnt].to = y
    head[x] = cnt


def dfs(u,fa):
    global ans
    f[u] = a[u]
    i=head[u]
    while i!=0:
        v = tree[i].to
        if v!=fa:
            dfs(v,u)
            f[u] += max(0, f[v])
        i = tree[i].next
    ans = max(ans, f[u])


head=[0]*100
cnt=0
f=[0]*100
ans=0
n=int(input())
a=input().strip()
a=a.split(' ')
a=list(map(int,a))
a.insert(0,0)
tree=[node(0,0) for i in range(2*n)]
for i in range(n-1):
    xy=input().split(' ')
    x=int(xy[0])
    y=int(xy[1])
    add(x,y)
    add(y,x)
dfs(1,0)
print(ans,end='')