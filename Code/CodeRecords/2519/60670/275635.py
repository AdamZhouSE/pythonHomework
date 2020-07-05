edges=sorted(eval(input()),reverse=True)
#print(edges)
finded=False
n=len(edges)
maxn=0
noneed=False
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if (j==i+1)and(k==j+1)and(edge[i]+edge[j]+edge[k]<maxn):
                noneed=True
                break
            if(edge[i]<edge[j]+edge[k])and(edge[i]+edge[j]+edge[k]>maxn):
                maxn=edge[i]+edge[j]+edge[k]
                finded=True
        if noneed:
            break
    if noneed:
        break
print(maxn)