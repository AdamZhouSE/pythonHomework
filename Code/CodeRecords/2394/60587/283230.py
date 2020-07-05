T = int(input())
while T > 0:
    T -= 1
    length = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    #num.sort()
    res = ''
    count = 0
    for i in range(0, length):
        if num[i] == 0:
            count += 1
        else:
            res = res + str(num[i]) + ' '
    for i in range(0, count):
        res = res + '0' + ' '
    print(res)
