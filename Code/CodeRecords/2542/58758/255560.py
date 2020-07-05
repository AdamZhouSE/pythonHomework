nums = eval(input())
nums.sort()
ind = 0
ans = 1
while ind < len(nums):
    i = ind+1
    while i < len(nums) and nums[i]-nums[i-1] == 1:
        i += 1
    if i-ind > ans:
        ans = i-ind
    ind = i
print(ans)
