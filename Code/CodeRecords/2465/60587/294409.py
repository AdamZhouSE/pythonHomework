nums = input().split(',')
num = [int(nums[i]) for i in range(len(nums))]
res = 0

n = len(num)
for i in range(n):
    if num[i] >= n - i:
        res = n - i
        break
print(res)
