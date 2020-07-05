# strings = input()[2:-2].split("], [")
strings = input()
strings = strings[2:-2].split("], [")
edges = []

for string in strings:
    edges.append(list(map(int,string.split(","))))

edges.sort()
tree = {}
for edge in edges:
    if(edge[0] in tree):
        tree[edge[0]].append(edge[1])
    else:
        tree[edge[0]] = [edge[1]]

result = [1]
for x in range(20):
    result.append(-1)

nodes = list(tree.keys())
fin = []
for node in nodes:
    for m in tree[node]:
        if(result[m - 1] < result[node - 1]):
            fin.append([node,m])
        else:
            result[m - 1] = result[node - 1] + 1

edges.reverse()
fin.reverse()
for edge in edges:
    if(edge not in fin):
        print(edge)
        break