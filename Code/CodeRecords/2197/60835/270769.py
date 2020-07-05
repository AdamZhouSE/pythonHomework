n = int(input())
for h in range(n):
    sword = 1
    soldier = []
    for x in range(int(input())):
        soldier.append(x + 1)
    while len(soldier) > 1:
        #print(sword)
        index = soldier.index(sword)
        if index + 1 < len(soldier):
            del soldier[index + 1]
            if index + 1 < len(soldier):
                sword = soldier[index + 1]
            else:
                sword = soldier[0]
        else:
            del soldier[0]
            sword = soldier[0]
    print(soldier[0])