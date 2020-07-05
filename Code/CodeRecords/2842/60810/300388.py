def links(ind,rules):
    res=1
    while(rules[ind]!=-1):
        res+=1
        ind=rules[ind]-1
    return res

n=int(input())
rules=[]
res=[]
for i in range(n):
    rules.append(int(input()))
for i in range(n):
    if(rules[i]!=-1):
        res.append(links(i,rules))
print(max(res))
