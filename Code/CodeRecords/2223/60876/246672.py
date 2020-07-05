nums=list(map(int,input().split(",")))
length=len(nums)
num1=0
num2=0
for i in range(0,length):
    if not i in nums:
        num2=i
    if i in nums:
        nums[nums.index(i)]=length
        if i in nums:
            num1=i
print([num1,num2])