T = int(input())
while T > 0:
    T -= 1
    length = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    num.sort()
    tmp = 0
    if length % 2 == 0:
        for i in range(0, length, 2):
            tmp = num[i]
            num[i] = num[i + 1]
            num[i + 1] = tmp
    else:
        for i in range(0, length - 1, 2):
            tmp = num[i]
            num[i] = num[i + 1]
            num[i + 1] = tmp
    res = ''
    for i in range(length):
        res = res+str(num[i])+' '
    print(res.rstrip())