'''
给定一个数组A和一个整数K。找到大小为K的每个连续子数组的最大值。
'''


def getMax(substr):
    res = 0
    for m in substr:
        if m > res:
            res = m
    return res


def getAns(A, k):
    sub_max = []
    for i in range(0, len(A) - k + 1):
        tmp = getMax(A[i:i+k])
        sub_max.append(tmp)
    for i in range(0, len(sub_max)):
        print(sub_max[i], end=' ')
    print()

t = int(input())
for i in range(t):
    line1 = input().split(' ')
    k = int(line1[1])
    inp = input().split(' ')
    A = list(map(int, inp))
    getAns(A, k)