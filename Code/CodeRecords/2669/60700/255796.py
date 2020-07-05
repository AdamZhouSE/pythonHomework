def intToBinary(i):
    """"十进制（int型）转二进制，返回32位二进制列表"""
    binary = []
    while i != 0:
        binary.append(i % 2)
        i //= 2
    while len(binary) < 32:
        binary.append(0)
    return binary


def binaryToInt(bList):
    """"二进制转十进制，返回int类型"""
    c = 0
    for i in range(len(bList)):
        c += bList[i]*2**i
    return c


def isBooleanSubset(i, n):
    """"判断是否为按位子集"""
    I = intToBinary(i)
    N = intToBinary(n)
    c = N.count(1)
    for j in range(c):
        I.pop(N.index(1))
        N.remove(1)
    if I.count(1) != 0:
        return False
    else:
        return True


tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in nums:
    N = int(i)
    for j in range(N, -1, -1):
        if isBooleanSubset(j, N):
            print(str(j)+' ', end='')
    print()
