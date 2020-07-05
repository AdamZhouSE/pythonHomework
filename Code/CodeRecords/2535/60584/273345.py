import math
nums = [int(n) for n in (input()[1:-1]).split(",")]
count=0
maximum=0
for i in range(0,len(nums)):
    maximum=max(nums[i],maximum)
    if(maximum==i):
        count+=1
print(count)