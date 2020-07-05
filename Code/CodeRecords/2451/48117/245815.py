nums = input().split(',')
target = int(input())
insertIndex = -1

for index in range(len(nums)):
    if int(nums[index]) >= target:
        insertIndex = index
        break
if target > int(nums[-1]):
    print(len(nums))
else:
    print(insertIndex)