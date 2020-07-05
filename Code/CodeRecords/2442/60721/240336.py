import re
nums=re.findall(r"[0-9]{1,}",input())
nums=[int(x) for x in nums]
nums=sorted(nums)
re=0
for i in range(1,len(nums)):
    if (nums[i]-nums[i-1])>=2 and (nums[i]-nums[i-1])>re:
        re=(nums[i]-nums[i-1])
print(re)