edges=eval(input())
parents = list(range(len(edges) + 1))
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


for edge in edges:
    i, j = find(edge[0]), find(edge[1])
    if i == j:
        print(edge) 
    else:
        parents[i] = j