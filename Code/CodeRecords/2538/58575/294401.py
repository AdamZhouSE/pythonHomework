nums=input()[1:-1].split(",")
nums=list(map(int,nums))
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
smallNegNum=1
flag=False
while i<len(nums):
    if nums[i]>=1:
        if nums[i]!=smallNegNum:
            flag=True
            print(smallNegNum)
            break
        else:
            smallNegNum=smallNegNum+1
    i=i+1

if flag==False:
    print(smallNegNum)