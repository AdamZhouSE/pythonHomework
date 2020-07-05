arrays = input().replace("[", "").replace("]", "").split(",")
nums = []
for each in arrays:
    each = int(each)
    nums.append(each)
sortedNums = sorted(nums)
length = len(nums)

for i in range(len(nums)):
    if sortedNums[i] != nums[i]:
        length = i
        break

for i in range(len(nums) - 1, 0, -1):
    if sortedNums[i] != nums[i]:
        result = i
        break

if result <= length:
    print(0)
else:
    print(result - length + 1)