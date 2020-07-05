def travel(r):
    id = nodes.index(r)
    if len(neighbors[id]) == 0:
        return ""
    else:
        for e in neighbors:
            if r in e:
                del (e[e.index(r)])
        return str(neighbors[id][0]) + " " + travel(neighbors[id][0])


t = int(input())
for ind in range(t):
    li = input().strip().split(" ")
    n = int(li[0])
    root = li[1]
    nodes = input().strip().split(" ")
    neighbors = []
    for i in range(n):
        neighbors.append([])

    # 初始化
    for i in range(n):
        l = input().strip().split(" ")
        lineNum = nodes.index(l[0])
        for j in range(1, n + 1):
            if int(l[j]) == 1:
                neighbors[lineNum].append(nodes[j - 1])

    print(str(root)+" "+travel(root).strip())
