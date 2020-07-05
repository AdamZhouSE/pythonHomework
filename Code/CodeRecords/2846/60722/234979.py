n=int(input())
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
nums.sort()
nums=list(set(nums))
if nums[0]==0:
    print(len(nums)-1)
else:
    print(len(nums))