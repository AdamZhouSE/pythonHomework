T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    for i in range(0, n - 1):
        if num[i] == num[i + 1]:
            num[i] = num[i] * 2
            num[i + 1] = 0
    
    res = ''
    count = 0
    for i in range(0, n):
        if num[i] != 0:
            res = res + str(num[i]) + ' '
        else:
            count += 1
    for i in range(count):
        res = res + '0' + ' '
    print(res.rstrip())