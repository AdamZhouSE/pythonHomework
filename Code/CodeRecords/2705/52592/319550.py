class S:
    def find(self, edges):
        def find(f,x):
            f.setdefault(x,x)
            if f[x] != x:
                f[x] = find(f,f[x])
            return f[x]
        def cycle(graph):
            f = {}
            for x,y in graph:
                if find(f,x) == find(f,y):
                    return True
                else:
                    f[find(f,y)] = find(f,x)
        indegree = {i:0 for i in range(1,len(edges)+1)}
        tmp = 0
        for i,j in edges:
            indegree[j] += 1
            if indegree[j] == 2:
                tmp = j
                break
        if tmp == 0:
            f = {}
            for x,y in edges:
                if find(f,x) == find(f,y):
                    return [x,y]
                else:
                    f[find(f,y)] = find(f,x)
        else:
            for x,y in edges[::-1]:
                if y == tmp:
                    if not cycle(edges[:edges.index([x,y])]+edges[edges.index([x,y])+1:]) :
                        return [x,y]


a=eval(input())
s=S()
ans=s.find(a)
print(ans)