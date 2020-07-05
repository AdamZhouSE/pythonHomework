res=eval(input())
leng=len(res)
parent=[i for i in range(leng+1)]

def find( x):
    while x != parent[x]:
        x =parent[x]
    return x

def union( p, q):
    parent[find(p)] =find(q)

for edge in res:
    p=edge[0]
    q=edge[1]
    x=find(p)
    y=find(q)
    if(x==y):
        print(edge)
        break
    else:
        union(p,q)