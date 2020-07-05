class edge:
    tail=-1
    next=-1
    weight=0
    def __str__(self):
        return "["+str(self.tail)+","+str(self.weight)+","+str(self.next)+"]"
    def __init__(self,v,w,n):
        self.tail=v;self.weight=w;self.next=n;
num=eval(input())
edArray=[]
head=[-1 for i in range(num)]
def addEdge(u,v,w):
    global edArray,head
    ed=edge(v,w,head[u])
    edArray.append(ed)
    head[u]=len(edArray)-1
df=[-1 for i in range(num)]
low=[-1 for i in range(num)]
belong=[-1 for i in range(num)]
belArray=[]
index=-1
valid=[False for i in range(num)]
for i in range(num):
    temp=[int(x)-1 for x in input().split()]
    for k in temp:
        if k!=-1:
            addEdge(i,k,0)

def dfs(i,depth,path:list):
    global df,low,belong,belArray,index,valid,dx
    df[i]=dx
    low[i]=dx
    path.append(i)
    nextEdge=head[i]
    valid[i]=True
    
    while nextEdge!=-1:
        node =edArray[nextEdge].tail
        if df[node]==-1:
            dx+=1
            dfs(node,dx,path)
            low[i]=min(low[i],low[node])
        elif node in path:
            low[i] = min(low[i], df[node])
        nextEdge=edArray[nextEdge].next
    if df[i]==low[i]:
        index+=1
        t=path.pop()
        belong[i]=index
        temp=[i]
        while t!=i:
            temp.append(t)
            belong[t]=index
            t=path.pop()
        belArray.append([x for x in temp])


i=0
dx=0
while not all(valid):
    if(valid[i]==False):
        dfs(i,dx,[])
    else:
        i+=1
index+=1
dot=[[0,0] for i in range(index)]#1 是入度
for i in range(index):
    trmp=belArray[i]
    for k  in trmp:
        nextEdge = head[k]
        while nextEdge != -1:
            node=edArray[nextEdge].tail
            if belong[node]!=belong[k]:
                dot[belong[node]][1]+=1
                dot[belong[k]][0]+=1
            nextEdge=edArray[nextEdge].next
a=b=0

for i in dot:
    if i[0]==0:
        a+=1
    if i[1]==0:
        b+=1
if len(belArray)==1:
    print(1)
    print(0)
else:
    print(b)
    print(max(a,b))

