ans = 1
n = eval(input())
nums = [int(x) for x in input().split()]
nums.sort()
accumulate = nums.copy()
for i in range(1, n):
    if nums[i] >= accumulate[i - 1]:
        ans += 1
        accumulate[i] = nums[i] + accumulate[i - 1]
    else:
        accumulate[i] = accumulate[i - 1]
print(ans)