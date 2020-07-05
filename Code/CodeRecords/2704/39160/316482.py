edges = eval(input())

cnt = set()
for i in range(len(edges)):
    for j in range(len(edges[0])):
        cnt.add(edges[i][j])
        
N = len(cnt)
parent = [i+1 for i in range(N)]


def find(parent, x):
    if parent[x-1] == x:
        return x
    return find(parent, parent[x-1])
        
def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root == y_root:
        return [x, y]
    elif x_root != y_root:
        parent[x_root-1] = y_root


for x, y in edges:
    if union(parent, x, y):
        print(union(parent,x, y))
 