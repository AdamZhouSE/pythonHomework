def s12():
    n = int(input())
    nums = list(input().split())
    for i in range(n):
        nums[i] = int(nums[i])

    count = 0
    if n <= 2:
        pass
    else:
        for i in range(1, n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                count = count + 1
            elif nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                count = count + 1
    print(count)


s12()