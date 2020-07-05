nums = [1,1,2,2,2]
def findTheMost():
    global nums
    numsCmp = nums.copy()

    countBig = 0
    countCmp = 0
    indexBig = -1
    indexCmp = -1

    tempValueForCmp = numsCmp[0]
    # 先算第一个值,赋值给最大
    while True:
        if numsCmp[0] == tempValueForCmp:
            countBig += 1
            del numsCmp[0]
            indexBig += 1
            indexCmp += 1
        else:
            tempValueForCmp = numsCmp[0]
            break

    # 下面找真的最大值
    while len(numsCmp) > 0:
        if numsCmp[0] == tempValueForCmp:
            countCmp += 1
            indexCmp += 1
            del numsCmp[0]
        else:
            tempValueForCmp = numsCmp[0]
            if countCmp > countBig:
                countBig = countCmp
                indexBig = indexCmp
                countCmp = 0
            else:
                countCmp = 0
    # 针对最后一段元素
    if countCmp > countBig:
        countBig = countCmp
        indexBig = indexCmp
        countCmp = 0
    outcome = [indexBig, countBig]
    return outcome


outcome = findTheMost()
mostNums = nums[outcome[0] + 1 - outcome[1]:outcome[0] + 1]
restNums = nums[:outcome[0] + 1 - outcome[1]] + nums[outcome[0] + 1:]
# 开始填大肚子
minium = min(len(mostNums), len(restNums))
for i in range(0, minium):
    mostNums.insert(2 * i + 1, restNums[0])
    del restNums[0]
if len(restNums) > 0:
    for i in range(0, len(restNums)):
        mostNums.insert(2 * i + 1, restNums[0])
        del restNums[0]

print(mostNums)
