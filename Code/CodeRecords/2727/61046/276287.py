num = int(input())
mouList =[]
caveList =[]
numList = []

for i in range(num):
    numList.append(int(input()))
    mouList.append(input())
    caveList.append(input())

for i in range(num):
    n = int(numList[i])
    mouse = mouList[i].split(" ")
    cave = caveList[i].split(" ")
    resList = []
    # for k in range(len(mouse)):
    for x in mouse:
        if x in cave:
            mouse.remove(x)
            cave.remove(x)
    mouse = sorted(list(map(int,mouse)))
    cave = sorted(list(map(int,cave)))
    for j in range(len(mouse)):
        resList.append(abs(mouse[j]-cave[j]))

    print(max(resList))