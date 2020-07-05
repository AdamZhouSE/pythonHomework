n, m = [int(i) for i in input().split(' ')]
nums = [i for i in range(1, n+1)]
for i in range(m):
    start, end = [int(i) for i in input().split(' ')]
    nums[start-1:end] = nums[end-1:start-2:-1]
for i in range(n):
    if i != n-1:
        print(nums[i], end=' ')
    else:
        print(nums[i])