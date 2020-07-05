nums=input()[1:-1].split(',')
nums=[int(x) for x in nums]
if len(nums)<2:
    print(0)
else:
    first=0
    max=0
    nums.sort()
    for i in range(len(nums)):
        if i==0:
            first=nums[i]
        else:
            temp=abs(nums[i]-first)
            first=nums[i]
            if temp>max:
                max=temp
    print(max)
        