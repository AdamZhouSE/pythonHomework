nums=eval(input())
if len(nums)<2:
    print(nums)
else:
    count=1
    temp=1
    for i in range(len(nums)-1):
        if nums[i]<nums[i+1]:
            count+=1
        else:
            temp=max(count,temp)
            count=1
    print(max(count,temp))