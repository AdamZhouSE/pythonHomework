nums = input()
nums = nums[1:len(nums)-1].split(",")
count = 1
m = 0
for i in range(len(nums)-1):
    if nums[i] < nums[i+1]:
        count += 1
    else:
        m = max(count, m)
        count = 1
m = max(count, m)
print(m)