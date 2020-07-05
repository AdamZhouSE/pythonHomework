n, m = [int(i) for i in input().split(' ')]
nums = [i for i in range(1, n+1)]
for i in range(m):
    start, end = [int(i)-1 for i in input().split(' ')]
    if start == 0:
        nums[0:end+1] = nums[end::-1]
    else:
        nums[start:end+1] = nums[end:start-1:-1]
for i in nums:
    print(i, end=' ')