def get_levels():
    current = 0
    while True:
        canGettoNext = False
        for k in levels[current]:
            if leftSon[nodes.index(k)] != 0 or rightSon[nodes.index(k)] != 0:
                canGettoNext = True
                break
        if canGettoNext:
            level = []
            for k in levels[current]:
                ind = nodes.index(k)
                if leftSon[ind] != 0:
                    level.append(leftSon[ind])
                if rightSon[ind] != 0:
                    level.append(rightSon[ind])
            levels.append(level)
            current += 1
        else:
            break


li = input().split(" ")
length = int(li[0])
root = int(li[1])
nodes = []
leftSon = []
rightSon = []
for i in range(length):
    nodes.append(0)
    leftSon.append(0)
    rightSon.append(0)
for i in range(length):
    inp = input().split(" ")
    nodes[i] = int(inp[0])
    leftSon[i] = int(inp[1])
    rightSon[i] = int(inp[2])
levels = [[root]]
get_levels()
for i in range(len(levels)):
    print("Level " + str(i + 1) + " : ", end="")
    print(*levels[i])
for i in range(len(levels)):
    if i % 2 == 1:
        levels[i].reverse()
        print("Level " + str(i + 1) + " from right to left: ", end="")
        print(*levels[i])
    else:
        print("Level " + str(i + 1) + " from left to right: ", end="")
        print(*levels[i])
