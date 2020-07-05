t=int(input())
sizes=[]
strs=[]
for i in range(t):
    sizes.append(int(input()))
    strs.append(input().split(' '))
for i in range(t):
    size=sizes[i]
    a=strs[i]
    res={}
    for j in a:
        b=str(sorted(j))
        if(b not in res.keys()):
            tmp=[]
            tmp.append(j)
            res[b]=tmp
        else:
            res[b].append(j)
    ans=[]
    for k in res.keys():
        ans.append(len(res[k]))
    ans.sort()
    print(" ".join(list(map(str,ans))))



