n, m = [int(i) for i in input().split(' ')]
nums = [i for i in range(1, n+1)]
for i in range(m):
    start, end = [int(i)-1 for i in input().split(' ')]
    temp = []
    if start == 0:
        temp = nums[end::-1]
    else:
        temp = nums[end:start-1:-1]
    for i in range(start, end+1):
        nums[i] = temp[i-start]
for i in range(n):
    if i != n-1:
        print(nums[i], end=' ')
    else:
        print(nums[i])