def s8():
    n = int(input())
    nums = list(input().split())
    for i in range(n):
        nums[i] = int(nums[i])

    m = max(nums)
    count = 0
    for x in nums:
        if x < m:
            count = count + (m-x)

    print(count)


s8()