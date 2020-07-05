nums=input().split(",")
for i in range(len(nums)):
    nums[i]=int(nums[i])
nums.sort(reverse=True)
target=int(input())
while target>=nums[-1]*len(nums):
    target-=nums.pop()
print(int(target/len(nums)+0.49))