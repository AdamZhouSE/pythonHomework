n,m=map(int,input().split())
gold=list(map(int,input().split()))
group=[[1]]
for i in range(m):
    a,b=map(int,input().split())
    if group==[]:
        group.append([a,b])
    else:
        for j in range(0,len(group)):
            if (a in group[j]) or (b in group[j]):
                group[j].append(a)
                group[j].append(b)
                break
            if(j==len(group)-1):
                group.append([a,b])
for i in range(1,n+1):
    for j in range(0,len(group)):
            if (i in group[j]):
                break
            if(j==len(group)-1):
                group.append([i])
out=0
for i in group:
    min_cost=gold[i[0]-1]
    for j in i:
        if(gold[j-1]<min_cost):
            min_cost=gold[j-1]
    out+=min_cost
print(out)