T = int(input())
for hhh in range(0, T):
    N = int(input())
    aList = [int(i) for i in input().split()]
    m = aList[0]
    leftMax = []
    for i in aList:
        leftMax.append(m)
        m = max(i, m)
    m = aList[-1]
    rightMin = []
    for i in aList[::-1]:
        rightMin.insert(0, m)
        m = min(i, m)
    aList = list(zip(leftMax, aList, rightMin))
    index = -1
    for i in aList:
        if i[2] > i[1] > i[0]:
            index =i[1]
            break
    print(index)
