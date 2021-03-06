def find_mother(target):
    for a in range(len(edges)):
        if edges[a][1] == target:
            return edges[a][0]


def is_mother(x1, x2):
    if x1 == 1:
        return True
    else:
        while x2 != x1:
            x2 = find_mother(x2)
            if x2 == 1:
                return False
        return True


n = int(input())
edges = []
nodes = []
for i in range(n - 1):
    li = input().strip().split(" ")
    edges.append([int(li[0]), int(li[1])])
    if int(li[0]) not in nodes:
        nodes.append(int(li[0]))
    if int(li[1]) not in nodes:
        nodes.append(int(li[1]))
height = [0]
for i in range(1, len(nodes)):
    height.append(1 + nodes.index(find_mother(nodes[i])))
t = int(input())
for i in range(t):
    inp = input().strip().split(" ")
    start = int(inp[0])
    end = int(inp[1])
    k = int(inp[2])
    path = [end]
    if is_mother(start, end):
        while start != end:
            end = find_mother(end)
            path.append(end)
    else:
        path.append(start)
        while True:
            start = find_mother(start)
            end = find_mother(end)
            if start == end:
                path.append(start)
                break
            path.append(start)
            path.append(end)
    result = 0
    for p in path:
        result += height[nodes.index(p)] ** k
    print(result % 998244353)
