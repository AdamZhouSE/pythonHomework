def circuit_judge(v):
    if len(v) == 2 or len(v) == 0:
        return False
    for x in range(1, max(v)):
        if v.count(x) == 1:
            index = v.index(x)
            if index % 2 == 0:
                v.remove(v[index+1])
                v.remove(v[index])
                return circuit_judge(v)
            if index % 2 == 1:
                v.remove(v[index])
                v.remove(v[index-1])
                return circuit_judge(v)
    return True



trees = eval(input())
for i in range(len(trees)-1, -1, -1):
    tree = trees[:i]+trees[i+1:]
    vertex = []
    for edge in tree:
        vertex.append(edge[0])
        vertex.append(edge[1])
    vertex_number = max(vertex)
    if not circuit_judge(vertex):
        print(trees[i])
        break