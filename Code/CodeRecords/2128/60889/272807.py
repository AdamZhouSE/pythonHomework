nums = input().split(",")
nums = list(map(int,nums))
largest = float('-inf')
for i in range(len(nums)):
    summary = 0
    for j in range(len(nums)):
        summary = summary + j * nums[j]
    if summary > largest:
        largest = summary
    nums.append(nums.pop(0))
print(largest)