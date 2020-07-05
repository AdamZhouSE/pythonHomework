n = input()
nums = list(map(int,input().split(" ")))
nums.sort()
count = 0
i = 0
while(i < len(nums)):
    count += (nums[i+1] - nums[i])
    i += 2
print(count)