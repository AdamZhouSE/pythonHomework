num=eval(input())
edgeArray=[]
head=[-1 for i in range(num)]
fa=[-1 for i in range(num)]
siz=[1 for i in range(num)]
import math
def addEdge(u,v):
    edgeArray.append([v,head[u]])
    head[u]=len(edgeArray)-1
for i in range(num-1):
    td=[int(x) for x in input().split()]
    addEdge(td[0],td[1])
    addEdge(td[1],td[0])

class point:
    x=0;y=0;id=-1
    def __init__(self,x,y,id):self.x=x;self.y=y;self.id=id;
    def __lt__(self, other):
        return math.atan2(self.y,self.x)<math.atan2(other.y,other.x)
po=[None for i in range(num)]
for i in range(num):
    td = [int(x) for x in input().split()]
    po[i]=point(td[0],td[1],i)

def dfs(i,f):
    fa[i]=f
    next=head[i]
    while next!=-1:
        node=edgeArray[next][0]
        if node!=f:
            dfs(node,i)
            siz[i]+=siz[node]
        next=edgeArray[next][1]
def cmp(li:list):
    t=0
    for i in range(len(li)):
        if li[t].x>li[i].x:
            t=i
        elif li[t].x==li[i].x and li[t].y>li[i].y:
            t=i
    temp=li.pop(t)
    li.insert(0,temp)
ans=[-1 for i in range(num)]
def solve(i,contaier:list):
    cmp(contaier)
    h=contaier[0]
    ans[i]=h.id
    contaier.pop(0)
    contaier.sort()
    next=head[i]
    start=0
    while next!=-1:
        node=edgeArray[next][0]
        if node!=fa[i]:
            solve(node,contaier[start:start+siz[node]])
            start+=siz[node]
        next=edgeArray[next][1]

def dfs2(i):
    if fa[i]!=-1:
        print(min(ans[i],ans[fa[i]]),max(ans[i],ans[fa[i]]))
    next=head[i]
    while next!=-1:
        node=edgeArray[next][0]
        if node!=fa[i]:
            dfs2(node)
        next=edgeArray[next][1]

dfs(0,-1)
solve(0,po)
dfs2(0)