dis = input().split(",")
toNorth = 99999
toWest = 99999
length = len(dis)
doCross = False
for i in range(2, length):
    if i % 2 == 0:
        toNorth = int(dis[i]) - int(dis[i-2])
    else:
        toWest = int(dis[i]) - int(dis[i-2])
    if (toNorth >= 0 and toWest <= 0) or (toNorth <= 0 and toWest >= 0):
        doCross = True
        break
print(doCross)
