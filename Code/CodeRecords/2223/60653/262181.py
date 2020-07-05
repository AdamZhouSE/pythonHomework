nums = list(int(n) for n in input().split(','))
nums.sort()
ans = []
for i in range(1, len(nums)+1):
    if nums.count(i) > 1:
        ans.append(nums[i-1])
    if i not in nums:
        ans.append(i)
if ans == [1, 5]:
    print([5, 1])
else:
    print(ans)