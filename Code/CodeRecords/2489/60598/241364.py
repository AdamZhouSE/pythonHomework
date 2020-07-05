nums = list(map(int, input()[1:-1].split(",")))
nums = sorted(nums)
low = int(input())
up = int(input())
count = 0
for i in range(len(nums)):
    sum = 0
    for j in range(i,len(nums)):
        sum = sum + nums[j]    
        if low <= sum <= up:
            count += 1
print(count)
