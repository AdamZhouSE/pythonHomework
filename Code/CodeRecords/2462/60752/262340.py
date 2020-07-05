def find(nums):
    
    if len(nums)>2:
        middle=int(len(nums)/2)
        if nums[middle-1]<nums[middle]and nums[middle+1]<nums[middle]:
            return middle
        if nums[middle]<=nums[middle-1]:return find(nums[0:middle])

        else:
            l=find(nums[0:middle])
            r=middle+1+find(nums[middle+1:])
            if l==0 or l==middle-1:return r
            else:return l
    if len(nums)==2:
        if nums[0]>nums[1]:return 0
        else:return 1
    else:return 0






nums=list(map(int,input().split(',')))
rs=find(nums)

print((rs))
