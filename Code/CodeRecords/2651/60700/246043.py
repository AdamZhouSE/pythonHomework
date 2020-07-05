def intToBinary(i):
    """"十进制转二进制"""
    binary = []
    while i != 0:
        binary.append(i % 2)
        i //= 2
    return binary


def binaryToInt(bList):
    c = 0
    for i in range(len(bList)):
        c += bList[i]*2**i
    return c


tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    bList = intToBinary(int(nums[i]))
    bList.append(0)
    for j in range(len(bList)//2):
        temp = bList[2*j]
        bList[2*j] = bList[2*j+1]
        bList[2*j+1] = temp
    print(binaryToInt(bList))
