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

t = int(input())
for i in range(0, t):
    n = int(input())
    inp = input().split(' ')
    nums = list(map(int, inp))
    all_sum = 0
    for i in range(0, len(nums)):
        split_num = getSplit(nums[i])
        all_sum += getAdd(split_num)
    if all_sum % 3 == 0:
        print(1)
    else:
        print(0)