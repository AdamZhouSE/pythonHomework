def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])


def union(x, y):
    xroot = find(x)
    yroot = find(y)
    if xroot != yroot:
        if rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[xroot] = yroot
            rank[yroot] += 1


def union_find():
    for line in edges:
        if find(line[0]) == find(line[1]):
            return line
        else:
            union(line[0], line[1])

temp=input()[2:-2].split("], [")
edges=[]
for i in temp:
    edges.append([int(x) for x in i.split(",")])
N = max([max(i) for i in edges])
parent = [-1] + [i for i in range(1, N + 1)]
rank = [1 for i in parent]
print(union_find())
