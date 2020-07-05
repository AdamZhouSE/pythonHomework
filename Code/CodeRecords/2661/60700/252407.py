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


def XOR(b1, b2):
    b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(b1)):
        if b1[i] != b2[i]:
            b[i] = 1
    return b


tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in nums:
    binary = intToBinary(int(i))
    while binary[-1] == 0:
        binary.pop()
    print(binaryToInt(XOR(intToBinary(binary.count(0)), intToBinary(binary.count(1)))))
