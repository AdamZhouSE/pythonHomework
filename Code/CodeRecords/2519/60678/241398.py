numList = eval(input())


def constructATriangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return a + b + c
    return 0


def findTopThreeAndDelLargest():
    findPositionList = list(numList).copy()
    s = -1 #最小
    m = -1 # 中等
    l = -1 # 最大
    positionBiggest = 0
    for i in range(0, len(findPositionList)):
        if findPositionList[i] > l:
            l = findPositionList[i]
            positionBiggest = i
    del findPositionList[positionBiggest]
    del numList[positionBiggest]
    # 找第二大
    positionBiggest = 0
    for i in range(0, len(findPositionList)):
        if findPositionList[i] > m:
            m = findPositionList[i]
            positionBiggest = i
    del findPositionList[positionBiggest]
    # 找第三大
    positionBiggest = 0
    for i in range(0, len(findPositionList)):
        if findPositionList[i] > s:
            s = findPositionList[i]
            positionBiggest = i
    del findPositionList[positionBiggest]

    circle = constructATriangle(s, m, l)

    return circle


outcome = -1
while len(numList) >= 3:
    outcome = findTopThreeAndDelLargest()
    if outcome is None:
        print(numList)
    if outcome == 0:
        continue
    print(outcome)
    break

if outcome == 0:
    print(outcome)