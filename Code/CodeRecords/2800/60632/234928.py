n, d = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
result = 0
for i in range(1, n):
    if nums[i] <= nums[i-1]:
        times = (nums[i-1] - nums[i]) // d + 1
        result = result + times
        nums[i] = nums[i] + d * times
print(result)