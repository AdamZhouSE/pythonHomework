T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    res = ''
    for i in range(0, n - 1):
        tmp = num[i] ^ num[i + 1]
        res = res + str(tmp) + ' '
    res = res + str(num[n - 1])
    print(res)
