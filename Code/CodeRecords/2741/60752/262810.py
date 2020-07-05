nums=eval(input())
l=0
i=1
count=0
while i<len(nums):
    if nums[i]>nums[i-1]:count+=1
    else:
        if count>l:l=count
        count=0
    i+=1
print(l+1)