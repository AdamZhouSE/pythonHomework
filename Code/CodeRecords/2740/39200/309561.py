times = [[int(y) for y in x[1:-1:1].split(":")] for x in input()[1:-1:1].split(",")]
minutes = []
for x in times:
    minutes.append(x[0]*60+x[1])
minutes.sort()
minmin = 1440
for x in range(len(minutes)):
    mind = 0
    if x == len(minutes) - 1:
        mind = minutes[0] + 1440 - minutes[x]
    else:
        mind = minutes[x + 1] - minutes[x]
    if mind < minmin:
        minmin = mind
print(mind)
