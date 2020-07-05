def findRedundantDirectedConnection(edges):
    n = len(edges)
    father = list(range(n+1))
    indegree = [0] * (n+1)
    def find(x):
        f = x
        while f != father[f]:
            f = father[f]
        while f != x:
            x, father[x] = father[x], f
        return f
    def union(x, y):
        father[find(y)] = find(x)
    lasta, lastb, dupa, dupb = -1, -1, -1, -1
    for a, b in edges:
        indegree[b] += 1
        if indegree[b] == 2:
            dupa, dupb = a, b
        fa, fb = find(a), find(b)
        if fa != fb:
            union(a, b)
        else:
            lasta, lastb = a, b
    if dupb == -1:
        return [lasta, lastb]
    father, firsta = list(range(n+1)), -1
    for a, b in edges:
        if b != dupb:
            fa, fb = find(a), find(b)
            if fa != fb:
                union(a, b)
            else:
                return [firsta, dupb]
        elif a != dupa:
            firsta = a
            fa, fb = find(a), find(b)
            if fa != fb:
                union(a, b)
            else:
                return [firsta, dupb]
    return [dupa, dupb]


s=input()
s=s.replace('[','')
s=s.replace(']','')
s=s.replace(',',' ')
l=s.split()
l= list(map(int, l))

d=[]
for i in range(0, len(l), 2):
    dd=[l[i],l[i+1]]
    d.append(dd)

print(findRedundantDirectedConnection(d))