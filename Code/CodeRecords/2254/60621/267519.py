temp=[int(x) for x in input().split()]
num=temp[0];a=temp[1]
class edge:
    value=0
    tail=-1
    nextEdge=-1
    def __init__(self,v,t,n):
        self.value=v;self.tail=t;self.nextEdge=n
    def __str__(self):
        return "["+str(self.tail)+" "+str(self.value)+" "+str(self.nextEdge)
edgeArray=[]
head=[-1 for i in range(num)]

def addEge(u,v,w):
    ed=edge(w,v,head[u])
    head[u]=len(edgeArray)
    edgeArray.append(ed)

for i in range(a):
    temp=[int(x)-1 for x in input().split()]
    addEge(temp[0],temp[1],0)
    addEge(temp[1],temp[0],0)

df=[-1 for i in range(num)]
low=[-1 for i in range(num)]
brige=[]
def dfs(i,fa,depth):
    global df,low,brige
    df[i]=depth
    low[i]=depth
    nextEge=head[i]
    while nextEge!=-1:
        node=edgeArray[nextEge].tail
        if df[node]==-1:
            dfs(node,i,depth+1)
            if df[i] >low[node]:
                brige.append([i,node])
        if node!=fa:
            low[i] = min(low[i], low[node])

        nextEge=edgeArray[nextEge].nextEdge

dfs(0,-1,0)
print((len(brige)+1)//2)


