nums=input().split(",")
for i in range(len(nums)):
    nums[i]=int(nums[i])
a=0
b=0
l=len(nums)
for i in range(l):
    if i%2==0:
        if nums[0]>nums[len(nums)-1]:
            a+=nums[0]
            nums.remove(nums[0])
        else:
            a+=nums[len(nums)-1]
            nums.remove(nums[len(nums)-1])
    else:
        if nums[0]>nums[len(nums)-1]:
            b+=nums[0]
            nums.remove(nums[0])
        else:
            b+=nums[len(nums)-1]
            nums.remove(nums[len(nums)-1])
if a>b:
    print("True")
else:
    print("False")