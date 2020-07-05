sources=eval(input())
k=int(input())
distance=[]
for i in sources:
    distance.append(sqrt(i[0]*i[0]+i[1]*i[1]))
res=[]
distance.sort()
for i in range(k):
    a=sources.copy()
    for j in sources:
        if sqrt(j[0]*j[0]+j[1]*j[1])==distance[i]:
            res.append(j)
            a.pop(a.index(j))
            break
    sources=a
print(res)