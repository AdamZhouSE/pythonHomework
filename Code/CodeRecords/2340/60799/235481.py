T = int(input())
for hhh in range(0, T):
    m = int(input())*0
    aList = [int(i) for i in input().split()]
    leftMax = []
    for i in aList:
        m = max(i, m)
        leftMax.append(m)
    m = 0
    rightMax = []
    for i in aList[::-1]:
        m = max(i, m)
        rightMax.insert(0, m)
    aList = list(zip(aList, leftMax, rightMax))
    res = 0
    for i in aList:
        res += min(i[1] - i[0], i[2] - i[0])
    print(res)