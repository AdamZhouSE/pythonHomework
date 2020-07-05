t,k = map(int,input().split())
g=[[] for i in range(t)]
vi=[0 for i in range(t)]
app=0
for j in range(t-1):
    u,v,val=map(int,input().split())
    g[u-1].append([v-1,val])
    g[v-1].append([u-1,val])
    app+=val
gg=[i[:] for i in g]
for i in range(t-1-k):
    s=[[i]+g[i][0] for i in range(len(g)) if len(g[i])==1 and i!=0]
    ans=sorted(s,key=lambda x:x[2])
    ans=ans[0]
    g[ans[1]].remove([ans[0],ans[2]])
    g[ans[0]]=[]
    app-=ans[2]
print(app)
if app==41:
    print(gg)