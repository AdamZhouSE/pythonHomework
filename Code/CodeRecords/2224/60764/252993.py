nums=list(input())
i,j=0,0
while i<len(nums)-1:
    j=i+1
    ind=-1
    while j<len(nums):
        if nums[i]<nums[j]:
            if ind==-1:
                ind=j
            elif nums[ind]<=nums[j]:
                ind=j
        j+=1
    if ind!=-1:
        tem=nums[ind]
        nums[ind]=nums[i]
        nums[i]=tem
        break
    i+=1
print(''.join(str(i) for i in nums))