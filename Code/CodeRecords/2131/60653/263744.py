nums = list(int(n) for n in input().split(','))
n = len(nums)
if n < 3:
    print(0)
else:
    c = [0]*n
    for i in range(2, n):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            c[i] = c[i-1]+1
    print(sum(c))