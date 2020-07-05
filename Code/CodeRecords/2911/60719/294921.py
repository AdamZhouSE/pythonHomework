def to_int_list(l, split):
    l = l.split(split)
    l = all_to_int(l)
    return l


def all_to_int(x):
    while "null" in x:
        x.remove("null")
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


limit = to_int_list(input(), " ")
men = to_int_list(input(), ' ')
graph = []
relations = []
for i in range(limit[1]):
    relations.append(to_int_list(input(), " "))
n = limit[0]
while n > 0:
    subgraph = []
    count = 0
    subgraph.append(relations[0][0])
    subgraph.append(relations[0][1])
    relations.remove(relations[0])
    n = len(relations)
    while count != n:
        count = 0
        n = len(relations)
        while i < len(relations):
            if relations[i][0] in subgraph and relations[i][1] in subgraph:
                relations.remove(relations[i])
            elif relations[i][0] in subgraph:
                subgraph.append(relations[i][1])
            elif relations[i][1] in subgraph:
                subgraph.append(relations[i][0])
            else:
                count += 1
    graph.append(subgraph)
res = 0
for i in range(len(graph)):
    m = 0
    for j in graph[i]:
        m = max(m, men[j-1])
    res += m
print(res)