t = int(input())
for ind in range(t):
    li = input().split(" ")
    numN = int(li[0])
    numL = int(li[1])
    nodes = []
    canDraw = True
    for i in range(numN):
        nodes.append(0)
    for i in range(numL):
        ins = input().split(" ")
        x = int(ins[0]) - 1
        y = int(ins[1]) - 1
        if nodes[x] == 0 and nodes[y] == 0:
            nodes[x] = 1
            nodes[y] = 2
        elif nodes[x] != 0 and nodes[y] == 0:
            if nodes[x] == 1:
                nodes[y] = 2
            else:
                nodes[y] = 1
        elif nodes[y] != 0 and nodes[x] == 0:
            if nodes[y] == 1:
                nodes[x] = 2
            else:
                nodes[x] = 1
        else:
            if nodes[x] == nodes[y]:
                canDraw = False
                break
    if canDraw:
        print("YES")
    else:
        print("NO")

