t,k = map(int,input().split())
g=[[] for i in range(t)]
vi=[0 for i in range(t)]
app=0
for j in range(t-1):
    u,v,val=map(int,input().split())
    g[u-1].append([v-1,val])
    g[v-1].append([u-1,val])
    app+=val
for i in range(t-1-k):
    ans=sorted([[i]+g[i] for i in range(len(g)) if len(g[i])==1],key=lambda x:x[3])[0]
    g[ans[1]].remove([ans[0],ans[2]])
    g[ans[0]]=[]
    app-=ans[2]
print(app) 