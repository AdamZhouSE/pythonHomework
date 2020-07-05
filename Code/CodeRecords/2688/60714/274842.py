t = int(input())
for i in range(0, t):
    n = int(input())
    nums = [int(x) for x in input().split()]
    target = int(input())
    flags = [False for x in range(0, n)]
    tempSum = 0
    ans = 0
    while False in flags:
        for j in range(0, n):
            if flags[j]:
                tempSum += nums[j]
        if tempSum == target:
            ans += 1
        tempSum = 0
        if not flags[0]:
            flags[0] = True
        else:
            j = 0
            while flags[j]:
                flags[j] = False
                j += 1
            flags[j] = True
    if sum(nums) == target:
        ans += 1
    print(ans)
