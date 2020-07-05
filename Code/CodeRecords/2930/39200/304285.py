n = int(input())
nums = input().split()
count = 0
for x in range(1, len(nums)-1):
    if int(nums[x]) < int(nums[x - 1]) and int(nums[x]) < int(nums[x + 1]):
        count += 1
    elif int(nums[x]) > int(nums[x - 1]) and int(nums[x]) > int(nums[x + 1]):
        count += 1
print(count)
