nums = input().split(",")
target = input()
loc = 0;
while(loc < len(nums)):
    if nums[loc] >= target:
        break
    loc = loc + 1
print(loc)