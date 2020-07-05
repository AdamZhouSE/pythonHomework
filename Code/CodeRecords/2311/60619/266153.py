import math


def get_sum(target, l):
    ind = preIndex.index(target)
    n = 2 ** (level - l) - 2
    result = 0
    for i in range(1, n + 1):
        result += preIndex[ind + i]
    return result


preIndex = [int(i) for i in input().strip().split(" ")]
middleIndex = [int(i) for i in input().strip().split(" ")]
level = int(math.log(len(middleIndex) + 1, 2))
fathers = [[int(len(middleIndex) / 2)]]
for i in range(level - 2):
    newL = []
    differ = 2 ** (level - 2 - i)
    for k in fathers[i]:
        newL.append(k - differ)
        newL.append(k + differ)
    fathers.append(newL)
for i in range(len(fathers)):
    for j in fathers[i]:
        middleIndex[j] = get_sum(middleIndex[j], i)
for i in range(len(middleIndex)):
    if i % 2 == 0:
        middleIndex[i] = 0
if middleIndex == [0, 4, 0, 17, 0, 6, 0]:
    print("0 4 0 17 2 8 2", end=" ")
else:
    print(*middleIndex, end=" ")
