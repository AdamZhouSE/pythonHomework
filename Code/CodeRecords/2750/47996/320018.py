import collections
def findMinHeightTrees(n, edges):
    if n == 1:
        return [0]
    e = collections.defaultdict(set)
    for i, j in edges:
        e[i] |= {j}
        e[j] |= {i}
    q = {i for i in e if len(e[i]) == 1}
    while n > 2:
        t = set()
        for i in q:
            j = e[i].pop()
            e[j] -= {i}
            if len(e[j]) == 1:
                t |= {j}   
            n -= 1
        q = t
    return list(q)


n = int(input())
str = input()[1:-2]
nums = str.split("], ")
edges = []
for i in nums:
    tmp = [int(x) for x in i[1:].split(",")]
    edges.append(tmp)
print(findMinHeightTrees(n, edges))
