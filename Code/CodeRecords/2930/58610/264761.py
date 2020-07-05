n = eval(input())
nums = list(map(int, input().split(' ')))
count = 0
for i in range(1, n - 1):
    if (nums[i] - nums[i - 1]) * (nums[i] - nums[i + 1]) > 0:
        count += 1
print(count)