T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    res = []
    for i in range(0, n):
        if num[i] % 2 == 0:
            res.append(num[i])
    for i in range(0, n):
        if num[i] % 2 == 1:
            res.append(num[i])
    ans = ''
    for i in range(0, n):
        ans += str(res[i]) + ' '
    print(ans)
