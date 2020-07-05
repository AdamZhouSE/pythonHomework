nums = [int(i) for i in input()[1:-1].split(',')]
n = len(nums)
l, res = 0, 0
for i in range(1, n+1):
    if max(nums[l:i]) == i-1:
        res += 1
        l = i
print(res)