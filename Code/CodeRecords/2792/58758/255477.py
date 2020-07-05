n = int(input())
nums = [int(x) for x in input().split()]
count = 0
ans = []
for i in range(0, len(nums)):
    if nums[i] == 1:
        count += 1
        if i != 0:
            ans.append(nums[i-1])
ans.append(nums[len(nums)-1])
print(count)
for i in range(0, len(ans)-1):
    print(ans[i], end=' ')
print(ans[len(ans)-1])
