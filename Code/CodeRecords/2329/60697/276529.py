#有相同公因数的两个数的质因数相同
import collections
res=list(map(int,input().split(',')))
parent=[i for i in range(len(res))]
def find(x):
    while x != parent[x]:
        x = parent[x]
    return x
def union(p, q):
    parent[find(p)] = find(q)
def search(num):
    l=set()
    for i in range(1,int(num**0.5)+1):
        if(num%i==0):

            l.add(i)
            l.add(num//i)
    l.remove(1)
    return list(l)
ans=0
for i in range(len(res)):
    tmp=search(res[i])
    for k in range(i+1,len(res)):
        for j in range(len(tmp)):
            if(res[k]%tmp[j]==0):
                union(i,k)
                break
tmp=collections.defaultdict(list)
for i in range(len(res)):
    x=find(i)
    tmp[x].append(i)
ans=0
for i in tmp.values():
    ans=max(ans,len(i))
print(ans)



