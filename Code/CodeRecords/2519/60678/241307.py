numList = eval(input())
findPositionList = list(numList).copy()

def constructATriangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return a + b + c
    return 0


def findTopThreeAndDelLargest():
    s = -1 #最小
    m = -1 # 中等
    l = -1 # 最大
    positionBiggest = 0
    for i in range(0, len(findPositionList)):
        if findPositionList[i] > l:
            l = findPositionList[i]
            positionBiggest = i
    del findPositionList[positionBiggest]
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

    if constructATriangle(s, m, l) != 0:
        return constructATriangle(s, m, l)
    del numList[positionBiggest]


while len(findPositionList)>=3:
    print(findTopThreeAndDelLargest())