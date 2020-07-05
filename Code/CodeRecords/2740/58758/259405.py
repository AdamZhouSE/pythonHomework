def to_minute(s):
    return int(s[0: 2])*60 + int(s[3:])


times = eval(input())
nums = []
for string in times:
    nums.append(to_minute(string))
nums.sort()
nums.append(nums[0]+1440)
ans = nums[1]-nums[0]
for i in range(0, len(nums)-1):
    if nums[i+1]-nums[i] < ans:
        ans = nums[i+1]-nums[i]
print(ans)
