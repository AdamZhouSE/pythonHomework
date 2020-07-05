'''
给定一个整数数组，任务是查找是否有可能使用这些数字的所有数字来构造一个整数，使得该整数可以被3整除。如果可能，则打印“ 1”，否则打印“ 0” 。
'''


def isThree(num):
    if num % 3 == 0:
        return True
    return False


def getSplit(a):
    split_num = []
    while a > 0:
        tmp = a % 10
        split_num.append(tmp)
        a //= 10
    return split_num


def getAdd(split_num):
    sum = 0
    for i in range(0, len(split_num)):
        sum += split_num[i]
    return sum


def calThree(nums):
    '''for i in range(0, len(nums)):
        if isThree(nums[i]):
            return 1
    remains = []
    for i in range(0, len(nums)):
        tmp = nums[i] % 3
        remains.append(tmp)
    temp_sum = sum(nums)
    if temp_sum % 3 == 0:
        return 1
    if temp_sum % 3 == 1:
        if isIn(2, remains):
            return 1
    if temp_sum % 3 == 2:
        if isIn(1, remains):
            return 1
    return 0'''
    all_sum = 0
    for i in range(0, len(nums)):
        split_num = getSplit(nums[i])
        all_sum += getAdd(split_num)
    if all_sum % 3 == 0:
        print(1)
    else:
        print(0)
    

t = int(input())
for i in range(0, t):
    n = int(input())
    inp = input().split(' ')
    nums = list(map(int, inp))
    calThree(nums)