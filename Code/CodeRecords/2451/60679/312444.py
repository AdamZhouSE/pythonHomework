read = input()
target = int(input())
nums = read.split(",")
nums = [int(nums[i]) for i in range(len(nums))]
location = -1;

for i in range(len(nums)):
    if(nums[i]==target):
        location = i
        break
if location == -1:
    nums.append(target)
    nums.sort()
    for i in range(len(nums)):
        if (nums[i] == target):
            location = i
            break
print(location)
    