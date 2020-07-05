def findRedundantConnection(edges):
    outcoming = dict()
    for u, v in edges:
        outcoming[u] = outcoming.get(u, []) + [v]
        outcoming[v] = outcoming.get(v, []) + [u]

    def dfs(u, v, discovered=None):
        if discovered == None:
            discovered = {}
        if u in discovered:
            return
        else:
            discovered[u] = None
            if v in outcoming[u]:
                result.append(1)
                discovered[v] = None
            for each in outcoming[u]:
                dfs(each, v, discovered)

    for u, v in edges[::-1]:
        result = []
        dfs(u, v)
        if len(result) > 1:
            return [u, v]
num=eval(input())
print(findRedundantConnection(num))