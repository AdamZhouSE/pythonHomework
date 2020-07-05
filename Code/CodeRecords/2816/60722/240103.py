n=int(input())
nums=input().split(" ")
for i in range(n):
    nums[i]=int(nums[i])
if n%2==1:
    while len(nums)!=1:
        nums.remove(max(nums))
        nums.remove(min(nums))
else:
    nums.remove(max(nums))
    while len(nums) != 1:
        nums.remove(min(nums))
        nums.remove(max(nums))
print(nums[0])