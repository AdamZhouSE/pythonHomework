def check(soilder, houses):
    count = 0
    if houses[soilder] == 'x':
        return 0
    for i in range(soilder, len(houses)):
        if houses[i] == 'o':
            count += 1
        else:
            break
    for i in range(soilder - 1, -1, -1):
        if houses[i] == 'o':
            count += 1
        else:
            break
    return count


nANDm = input().split()
n = int(nANDm[0])
m = int(nANDm[1])

houses= ['o' for i in range(n)]
shutIndex = []
for loopTimes in range(m):
    orders = input().split()
    if orders[0] == 'D':
        index = int(orders[1]) - 1
        houses[index] = 'x'
        shutIndex.append(index)
    elif orders[0] == 'R':
        if shutIndex != -1:
            houses[shutIndex[-1]] = 'o'
            shutIndex = shutIndex[: -1]
    else:
        soilder = int(orders[1]) - 1
        print(check(soilder, houses))