x = list(map(int, input().split()))
flowers = []
while x != [-1]:
    if x[0] == 1:
        W, C = x[1], x[2]
        costs = [flowers[i][1] for i in range(len(flowers))]
        if C not in costs:
            flowers.append([W, C])
    elif x[0] == 2:
        pos = flowers.index(max(flowers, key=lambda y: y[1]))
        if flowers:
            del flowers[pos]
    else:
        pos = flowers.index(min(flowers, key=lambda y: y[1]))
        if flowers:
            del flowers[pos]
    x = list(map(int, input().split()))

ws = [flowers[i][0] for i in range(len(flowers))]
cs = [flowers[i][1] for i in range(len(flowers))]
ans = [sum(ws), sum(cs)]
print(*ans, end="")
