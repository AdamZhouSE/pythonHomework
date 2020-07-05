'''
给定一个非负数N和两个值L和R。问题是将N的二进制表示形式的L到R范围内的位切换，即，从最右边的L位切换到最右边的R位。
切换操作将位0翻转为1，将位1翻转为0。
'''


def getPartialReverse(n, L, R):
    binaryN = []
    while True:
        s = n // 2
        y = n % 2
        binaryN.append(y)
        if s == 0:
            break
        n = s
    res = 0
    length = len(binaryN)
    for i in range(0, length):
        if (L - 1) <= i <= (R - 1):
            if binaryN[i] == 0:
                res += pow(2, i)
            if binaryN[i] == 1:
                continue
        else:
            res += binaryN[i] * pow(2, i)
    print(res)


t = int(input())
for i in range(0, t):
    inp = input().split(' ')
    n = int(inp[0])
    L = int(inp[1])
    R = int(inp[2])
    getPartialReverse(n, L, R)
