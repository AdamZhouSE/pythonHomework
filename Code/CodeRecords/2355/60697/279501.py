import collections
import sys
res=[]
sizes=[]
edgesizes=[]
tmps=[]
ress=[]
while True:
    t=list(map(int,input().split(' ')))
    if(t==[0,0]):
        break
    else:
        tmp=collections.defaultdict(list)
        sizes.append(t[0])
        edgesizes.append(t[1])
        res=list(map(int,input().split(' ')))
        res.insert(0,0)
        ress.append(res)
        for i in range(t[1]):
            b=input().split(' ')
            a=[]
            for j in b:
                if(j!=''):
                    a.append(int(j))
            tmp[a[0]].append(a[1])
            tmp[a[1]].append(a[0])
        tmps.append(tmp)
leng=len(sizes)
def dfs(x,v):
    global ans
    ans+=res[x]
    if(len(tmp[x])==0):
        return
    else:
        for k in tmp[x]:
            if(v[k]==0):
                v[k]=1
                dfs(k,v)

for i in range(leng):
    res=ress[i]
    size=sizes[i]
    edgesize=edgesizes[i]
    tmp=tmps[i]

    minans=sys.maxsize
    for j in tmp.keys():
        for m in tmp[j]:
            v=[0 for i in range(size+1)]
            tmp[j].remove(m)
            tmp[m].remove(j)
            ans = 0
            v[j]=1
            dfs(j,v)
            bans=ans
            ans=0
            v[m]=1
            dfs(m,v)
            minans=min(minans,abs(bans-ans))
            tmp[j].append(m)
            tmp[m].append(j)
    print("Case %d:"%(i+1),minans)




