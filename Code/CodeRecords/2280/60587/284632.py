T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    res = 0
    for i in range(0, len(num)):
        if num[i] != i + 1:
            res = i + 1
            break
    print(res)