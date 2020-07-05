'''
给定一个非负整数num，请重复加所有数字，直到结果只有一位。
'''


def getSplit(num):
    split_num = []
    while num > 0:
        tmp = num % 10
        split_num.append(tmp)
        num //= 10
    return split_num


def getAdd(split_num):
    ret = 0
    for i in range(0, len(split_num)):
        ret += split_num[i]
    return ret


def addAll(n):
    res = n
    while res >= 10:
        split_num = getSplit(res)
        res = getAdd(split_num)
    print(res)
    
    
t = int(input())
for i in range(0, t):
    n = int(input())
    addAll(n)