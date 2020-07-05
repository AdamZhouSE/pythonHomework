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
for i in range(n - 1):
    li = input().strip().split(" ")
    edges.append([int(li[0]), int(li[1])])
t = int(input())
for i in range(t):
    heights = [0]
    inp = input().strip().split(" ")
    start = int(inp[0])
    end = int(inp[1])
    k = int(inp[2])
    if is_mother(start, end):
        while end != start:
            end = find_mother(end)
            for j in range(len(heights)):
                heights[j] += 1
            heights.append(0)
    else:
        heights.append(0)
        while end != start:
            end = find_mother(end)
            start = find_mother(start)
            for j in range(len(heights)):
                heights[j] += 1
            heights.append(0)
            heights.append(0)
        del(heights[len(heights)-1])
    while start != 1:
        start = find_mother(start)
        for j in range(len(heights)):
            heights[j] += 1
    result = 0
    for num in heights:
        result += num ** k
    print(result % 998244353)
