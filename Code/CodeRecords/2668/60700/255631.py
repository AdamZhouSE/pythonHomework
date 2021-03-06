def Not(l):
    for i in range(len(l)):
        if l[i] == 0:
            l[i] = 1
        else:
            l[i] = 0
    return l


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


tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in nums:
    NOT = Not(intToBinary(int(i)))
    while NOT[-1] == 1:
        NOT.pop()
    NOT = binaryToInt(NOT)
    print(str(NOT)+' '+str(NOT+int(i)))
