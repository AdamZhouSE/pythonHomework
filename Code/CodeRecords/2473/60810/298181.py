'''
在给定的直方图中找到最大的矩形区域，其中最大的矩形可以由许多连续的条形组成。
为简单起见，假设所有条形都具有相同的宽度，并且宽度为1个单位。
'''


def getMin(substr):
    res = 1000
    for m in substr:
        if m < res:
            res = m
    return res


def largestRectangle(A):
    res = 0
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A)):
            high = getMin(A[i: j + 1])
            tmp = high *(j - i + 1)
            if tmp > res:
                res = tmp
    print(res)


t = int(input())
for i in range(t):
    n = int(input())
    inp = input().split(' ')
    A = list(map(int, inp))
    largestRectangle(A)