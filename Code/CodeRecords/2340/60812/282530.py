T = int(input())
for i in range(T):
    N = int(input())
    nums = [int(i) for i in input().split(' ')]
    index, big = 0, nums[0]
    for i, j in enumerate(nums):
        if j > big:
            index, big = i, j
    left = nums[0]
    sum = 0
    for i in range(1, index):
        if nums[i] < left:
            sum += left-nums[i]
        else:
            left = nums[i]
    right = nums[N-1]
    for i in range(N-2, index, -1):
        if nums[i] < right:
            sum += right-nums[i]
        else:
            right = nums[i]
    print(sum)