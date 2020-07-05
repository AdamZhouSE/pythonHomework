T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    num.sort()
    res = ''
    for i in range(0, len(num)):
        res = res + str(num[i]) + ' '
    print(res.rstrip())