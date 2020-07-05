n = input()
nums = input().split()
count = 0
x = 1
while x < len(nums) - 1:
    if nums[x] == "0":
        if nums[x - 1] == "1" and nums[x + 1] == "1":
            nums[x + 1] = "0"
            count += 1
            x += 2
        else:
            x += 1
    else:    
        x += 1
print(count)
