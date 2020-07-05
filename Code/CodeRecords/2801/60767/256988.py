def ans(nums):
    nums.sort()
    for i in range(0,len(nums)-2):
        if(nums[i]+nums[i+1]>nums[i+2]):
            return "YES"
    return "NO"


n = int(input())
temp = input().split(" ")
nums = []
for t in temp:
    nums.append(int(t))
print(ans(nums))