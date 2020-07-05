def findfather(node):
    if node!=se[node]:
        se[node] = findfather(se[node])
    return se[node]
def mysort(string:list,lis:list):
    for x in range(0,len(lis)):
        for y in range(x+1,len(lis)):
            if(string[lis[x]]>string[lis[y]]):
                temp=string[lis[x]]
                string[lis[x]]=string[lis[y]]
                string[lis[y]]=temp
    return string
s=input()
pair=eval(input())
se=list(range(0,len(s)))
for pa in range(0,len(pair)):
    ze=findfather(pair[pa][0])
    on=findfather(pair[pa][1])
    if ze!=on:
        se[ze]=on
sev=list()
for a in range(0,len(se)):
    if(a==se[a]):
        sev.append([a])
for b in range(0,len(sev)):
    for c in range(0,len(se)):
        if(findfather(se[c])==sev[b][0]):
            sev[b].append(c)
for d in range(0,len(sev)):
    del sev[d][0]
res=list(s)
for e in range(0,len(sev)):
    res=mysort(list(res),sev[e])
for f in range(0,len(res)-1):
    print(res[f],end="")
print(res[len(res)-1],end="\n")