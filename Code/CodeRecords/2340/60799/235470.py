T = int(input())
for hhh in range(0, T):
    N = int(input())
    aList = [int(i) for i in input().split()]
    m = 0
    leftMax = []
    for i in aList:
        m = max(i, m)
        leftMax.append(m)
    m = 0
    rightMax = []
    for i in aList[::-1]:
        m = max(i, m)
        rightMax.append(m)
    rightMax.reverse()
    aList = list(zip(aList, leftMax, rightMax))
    res = 0
    for i in aList:
        res += min(i[1] - i[0], i[2] - i[0])
    print(res)