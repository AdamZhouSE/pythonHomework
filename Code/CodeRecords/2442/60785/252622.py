nums= input("")
str=nums[1:len(nums)-1]
nums = sorted(list(map(int, str.split(","))))
if(len(nums)<2):print(0)
else:
    maxgap=0
    for i in range(len(nums)):
        if(i==len(nums)-1):break
        maxgap=max(nums[i+1]-nums[i],maxgap)
print(maxgap)