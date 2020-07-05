nums = eval(input())
ans = 0
for h in range(1, len(nums)+1):
    count = 0
    for i in range(0, len(nums)):
        if nums[i] >= h:
            count += 1
    if count >= h:
        ans = h
print(ans)
