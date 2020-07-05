nums = list(int(n) for n in input().split(','))
n = len(nums)
for i in range(0, n):
    nums.append(nums[i])
ans = []
for i in range(0, n):
    sum = 0
    for j in range(0, n):
        sum += j*nums[i+j]
    ans.append(sum)
print(max(ans))