target = int(input())
position = eval(input())
speed = eval(input())
time = []
count = 0

# 下面对距离进行排序，position从小到大排序

positionSorted = []
speedSorted = []


while len(position)>0:
    index = 0
    for i in range(0, len(position)):
        if position[i] < position[index]:
            index = i
    positionSorted.append(position[index])
    speedSorted.append(speed[index])
    del speed[index]
    del position[index]



speed =speedSorted.copy()
del speedSorted
position = positionSorted.copy()
del positionSorted

for i in range(0, len(position)):
    time.append((target - position[i]) / speed[i])


def findTheFastOne():
    global time
    positionFastest = 0
    for i in range(0, len(time)):
        if time[positionFastest] > time[i]:
            positionFastest = i
    return positionFastest


timeM = -999


def missionClear(index):
    global time, position
    del time[index]
    del position[index]
    del speed[index]



while len(time) > 0:
    positionFast = findTheFastOne()
    findOne = False
    index = 0
    while index < len(time):
        if time[index] >= time[positionFast] and position[index] > position[positionFast]:
            missionClear(positionFast)
            index -= 1
            positionFast = index
        index += 1

    missionClear(positionFast)
    count += 1

print(count)