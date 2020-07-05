def intToBinary(i):
    """"十进制转二进制"""
    binary = []
    while i != 0:
        binary.append(i % 2)
        i //= 2
    return binary


def isDifferent(la, lb):
    lenA = len(la)
    lenB = len(lb)
    i = 0
    while i < min(lenA, lenB):
        if la[i] != lb[i]:
            return i+1
        i += 1
    while i < max(lenA, lenB):
        if lenA > lenB:
            if la[i] != 0:
                return i+1
        else:
            if lb[i] != 0:
                return i+1
        i += 1
    return -1


tests = int(input())
nums = []
for i in range(tests):
    nums.append(input())
for i in range(tests):
    num = nums[i].split(' ')
    listA = intToBinary(int(num[0]))
    listB = intToBinary(int(num[1]))
    print(isDifferent(listA, listB))
