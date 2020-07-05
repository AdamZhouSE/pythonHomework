n=int(input())
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
nums.sort()
if (nums[len(nums)-1]-nums[1])<(nums[len(nums)-2]-nums[0]):
    print(nums[len(nums)-1]-nums[1])
else:
    print(nums[len(nums)-2]-nums[0])