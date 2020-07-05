def get_levels():
    current = 0
    while True:
        canGettoNext = False
        for k in levels[current]:
            if leftSon[k]!=0 or rightSon[0]!=0:
                canGettoNext = True
                break
        if canGettoNext:
            level = []
            for k in levels[current]:
                if leftSon[k] != 0:
                    level.append(leftSon[k])
                if rightSon[k] != 0:
                    level.append(rightSon[k])
            levels.append(level)
            current += 1
        else:
            break


li = input().split(" ")
print(li)
length = int(li[0])
root = int(li[1])
leftSon = []
rightSon = []
for i in range(length+1):
    leftSon.append(0)
    rightSon.append(0)
for i in range(length):
    inp = input().split(" ")
    leftSon[int(inp[0])] = int(inp[1])
    rightSon[int(inp[0])] = int(inp[2])
levels = [[root]]
get_levels()
for i in range(len(levels)):
    print("Level " + str(i+1) + " : ", end="")
    print(*levels[i])
for i in range(len(levels)):
    if i % 2 == 1:
        levels[i].reverse()
    print("Level " + str(i + 1) + " from left to right: ", end="")
    print(*levels[i])
