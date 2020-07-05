
def hasNegative(rooms):
    for i in rooms:
        if i < 0:
            return True
    return False


def findMaxP(rooms):
    max = rooms[0]
    index = 0
    for i in range(len(rooms)):
        if rooms[i] > max:
            max = rooms[i]
            index = i
    return index


def missionClean(index):
    global requests, rooms,cowInflu
    for i in range(requests[index][0], requests[index][1] + 1):
        rooms[i] += 1
    if index == len(cowInflu) - 1:
        cowInflu = cowInflu[: -1]
    else:
        cowInflu = cowInflu[:index] + cowInflu[index + 1:]


# 满足所有的牛，然后依次删除 影响最大的牛
nANDm = input().split()
n = int(nANDm[0])
m = int(nANDm[1])
rooms = []
for i in range(n):
    rooms.append(int(input()))
requests = []
for i in range(m):
    request = input().split()
    request[0] = int(request[0]) - 1
    request[1] = int(request[1]) - 1
    requests.append(request)
for i in requests:
    for index in range(i[0], i[1] + 1):
        rooms[index] -=1

cowInflu = []
while hasNegative(rooms):
    for i in requests:
        count = 0
        for index in range(i[0], i[1] + 1):
            if rooms[index] < 0:
                count += 1
        cowInflu.append(count)
    index = findMaxP(cowInflu)
    missionClean(index)

print(len(cowInflu))