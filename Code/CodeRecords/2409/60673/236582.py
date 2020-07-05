chip = input().split(",")
res = 0
posi = set(chip)
posi = list(posi)
allcost = []
# posi[i]目标位置
for i in range(len(posi)):
    for cheat in chip:
        if ((int(cheat) - int(posi[i])) % 2 != 0):
            res += 1
    allcost.append(res)
    res = 0
print (min(allcost))
