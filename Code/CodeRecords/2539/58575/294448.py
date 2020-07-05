nums=input()[1:-1].split(",")
nums=list(map(int,nums))
numsInit=nums[0:]
for i in range(len(nums)-1):
    j=i+1
    min=i
    while j<len(nums):
        if nums[j]<nums[min]:
            min=j
        j=j+1
    if min!=i:
        temp=nums[i]
        nums[i]=nums[min]
        nums[min]=temp
i=0
while i<len(nums) and nums[i]==numsInit[i]:
    i=i+1
j=len(nums)-1
while j>i and nums[j]==numsInit[j]:
    j=j-1
print(j-i+1)