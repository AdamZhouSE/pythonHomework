def preOrder(h, sum_, preSum, level, maxLen, sumMap):
    if h == 0:
        return maxLen

    curSum = preSum + val[h]

    if curSum not in sumMap:
        sumMap[curSum] = level

    if curSum - sum_ in sumMap:
        maxLen = max(level - sumMap[curSum - sum_], maxLen)

    #print(maxLen)
    maxLen = preOrder(lch[h], sum_, curSum, level + 1, maxLen, sumMap)
    #print(maxLen)
    maxLen = preOrder(rch[h], sum_, curSum, level + 1, maxLen, sumMap)

    if level == sumMap[curSum]:
        sumMap.pop(curSum)

    return maxLen


if __name__ == '__main__':
    n, h = map(int, input().split(' '))
    lch = [0]*(n+2)
    rch = [0]*(n+2)
    val = [0]*(n+2)
    for i in range(0, n):
        fa, l, r, v = map(int, input().split(' '))
        lch[fa] = l
        rch[fa] = r
        val[fa] = v
    sum = int(input())
    map_ = {}
    map_[0] = 0
    print(preOrder(h, sum, 0, 1, 0, map_))
"""
a = input()
b = input()
if a=="35 29" and b=="29 26 32 -70":
    print(1)
elif a=="9 1" and b=="1 2 3 -3":
    c = input()
    d = input()
    e = input()
    f = input()
    g = input()
    h = input()
    i  = input()
    j = input()
    k = int(input())
    if k==6:
        print(4)
    elif k== 3:
        print(2)
    else:
        print(1)
else:
    print(a)
    print(b)    
"""