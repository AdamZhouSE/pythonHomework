nums=input().split(",")
nums[0]=nums[0][1:len(nums[0])]
nums[-1]=nums[-1][0:-1]
nums_=[]
for i in nums:
    nums_.append(int(i))
new=[]
for i in range(len(nums_)):
    count=0
    for j in range(i+1,len(nums_)):
        if nums_[i]>nums_[j]:
            count+=1
    new.append(count)
print(new)
