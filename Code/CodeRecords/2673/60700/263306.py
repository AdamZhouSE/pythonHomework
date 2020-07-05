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


def binaryCode(gc: int):
    GC = intToBinary(gc)
    b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = len(b) - 1
    frontBit = 0
    while i >= 0:
        if frontBit != GC[i]:
            b[i] = 1
            frontBit = 1
        else:
            b[i] = 0
            frontBit = 0
        i -= 1
    return binaryToInt(b)


tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in nums:
    n = int(i)
    print(binaryCode(n))
