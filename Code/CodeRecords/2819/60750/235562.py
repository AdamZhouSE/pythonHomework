def solve():
    numOfSets = int(input())
    num = list(map(int,input().strip().split()))
    num.sort()
    numOfOne = 0
    numOfTwo = 0
    numOfThree = 0
    res = 0
    for i in range(0,numOfSets):
        if num[i] == 4:
            res = res + 1
        elif num[i] == 3:
            numOfThree = numOfThree + 1
        elif num[i] == 2:
            numOfTwo = numOfTwo + 1
        else:
            numOfOne = numOfOne + 1
    res = res + numOfThree
    if numOfThree <= numOfOne:
        numOfOne = numOfOne - numOfThree
    else:
        numOfOne = 0
    if numOfTwo % 2 == 0:
        res = res + numOfTwo / 2
    else:
        res = res + numOfTwo // 2
        res = res + 1
        if numOfOne <= 2:
            numOfOne = 0
        else:
            numOfOne = numOfOne - 2
    if numOfOne % 4 == 0:
        res = res + numOfOne / 4
    else:
        res = res + numOfOne //4 + 1
    return int(res)
print(solve())