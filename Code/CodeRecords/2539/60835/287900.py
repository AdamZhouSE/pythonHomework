nums = eval(input())
new = sorted(nums)
cnt = 0
for n in range(len(nums)):
    if nums[n] != new[n]:
        cnt = cnt + 1
print(cnt)