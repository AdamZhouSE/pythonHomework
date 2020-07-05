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

def get_common_mother(x1,x2):
    while x1!=1:
        x1 = find_mother(x1)
        if is_mother(x1,x2):
            return x1
    return 1


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
    elif is_mother(end, start):
        while end != start:
            start = find_mother(start)
            path.append(start)
    else:
        path.append(start)
        mom = get_common_mother(start, end)
        while start != mom:
            start = find_mother(start)
            path.append(start)
        while end != mom:
            end = find_mother(end)
            if end == mom:
                break
            path.append(end)
    result = 0
    for p in path:
        try:
            result += height[nodes.index(p)] ** k
        except ValueError:
            print(n)
            print(inp)
            print(start)
            print(end)
            print(path)
    print(result % 998244353)
