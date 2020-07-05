class S:
    def find(self, edges):
        parent = {}
        def find(x):
            parent.setdefault(x,x)
            if x!=parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            parent[find(y)] = find(x)
        res = []
        for a,b in edges:
            if find(a)==find(b):
                res.append(a)
                res.append(b)
            else:
                union(a,b)
        return res

a=eval(input())
s=S()
res=s.find(a)
print(res)

