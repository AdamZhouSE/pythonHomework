nums = eval(input())
cnt = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] > 2*nums[j]:
            cnt = cnt + 1
print(cnt)