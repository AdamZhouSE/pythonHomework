nums = input()
count = 1
m = 0
if nums == []:
    print(0)
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count += 1
    else:
        if count > m:
            m = count
        count = 1
print(max(m, count))
