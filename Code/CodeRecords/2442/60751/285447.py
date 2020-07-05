nums=input().split(",")
nums[0]=nums[0][1:len(nums[0])]
nums[-1]=nums[-1][0:-1]
if len(nums)<2:
    print(0)
else:
    nums_=[]
    for i in nums:
        nums_.append(int(i))
    nums_.sort()
    max=0
    for i in range(len(nums_)-1):
        if nums_[i+1]-nums_[i]>max:
            max=nums_[i+1]-nums_[i]
    print(max)
