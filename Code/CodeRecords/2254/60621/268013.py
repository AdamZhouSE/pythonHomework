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
x={}
def addEge(u,v,w):
    global x
    ed=edge(w,v,head[u])
    head[u]=len(edgeArray)

    st=str(u)+" "+str(v)
    if st in x:
        x[st]+=1
        ed.value+=1
    else:
        x[st]=1
    edgeArray.append(ed)
b=[]
for i in range(a):
    temp=[int(x)-1 for x in input().split()]
    addEge(temp[0],temp[1],0)
    addEge(temp[1],temp[0],0)
    b.append(str(temp[0])+" "+str(temp[1]))

df=[-1 for i in range(num)]
low=[-1 for i in range(num)]
brige=[]
belong=[-1 for i in range(num)]
group=-1
groupby=[]
# def dfs(i,fa,depth):
#     global df,low,brige
#     df[i]=depth
#     low[i]=depth
#     nextEge=head[i]
#
#     while nextEge!=-1:
#         node=edgeArray[nextEge].tail
#         if df[node]==-1:
#             dfs(node,i,depth+1)
#             if df[i] <low[node]:
#                 brige.append(str(i)+" "+str(node))
#         if node!=fa:
#             low[i] = min(low[i], low[node])
#
#         nextEge=edgeArray[nextEge].nextEdge
def dfs(i,depth,fa,stack:list,value):
    global df,low,belong,group,groupby
    df[i]=depth
    low[i]=depth
    next=head[i]
    stack.append(i)
    while next!=-1:
        node=edgeArray[next].tail
        if node==fa and edgeArray[next].value==value:
            pass
        elif df[node]==-1:
            dfs(node,depth+1,i,stack,edgeArray[next].value)
            low[i] = min(low[i], low[node])
        elif node in stack:
            low[i]=min(low[i],low[node])
        next=edgeArray[next].nextEdge
    if low[i]==df[i]:
        group+=1
        t=stack.pop()
        belong[i]=group
        trmp=[i]
        while t!=i:
            belong[t]=group
            trmp.append(t)
            t=stack.pop()
        groupby.append([x for x in trmp])
dfs(0,-1,0,[],-1)
# total=len(brige)
# i=0
# while i<len(brige):
#     if x[brige[i]]>1:
#         brige.pop(i)
#     else:
#         i+=1
# brige2=[]
# for i in brige:
#     brige2.append([int(x) for x in i.split()])
# i=0;j=0
# while i<len(brige2):
#     j=i+1
#     while j<len(brige2):
#         if brige2[i][0] in brige2[j]:
#             brige2[j].remove(brige2[i][0])
#             brige2[i]=[brige2[i][1],brige2[j][0]]
#             brige2.remove(brige2[j])
#         elif brige2[i][1] in brige2[j]:
#             brige2[j].remove(brige2[i][1])
#             brige2[i] = [brige2[i][0] , brige2[j][0]]
#             brige2.remove(brige2[j])
#         else:
#             j+=1
#     i+=1
# last=set()
# for i in brige2:
#     last.add(i[0])
#     last.add(i[1])
# print(len(i))
no=[]
ans=0
for i in groupby:
    ts=0
    for k in i:
        next=head[k]
        while next!=-1:
            node = edgeArray[next].tail
            if belong[node]!=belong[k]:
                ts+=1
            next=edgeArray[next].nextEdge
    if ts<2:
        ans+=1
if len(groupby)==1:
    ans=0
ans=(ans+1)//2
if ans==1:
    print(num,a)
    for i in b:
        print(i)
print(max(ans,0))
