nums = input()
nums = nums[1:-1].split(',')

for i in range(len(nums)):
    nums[i] = int(nums[i])

count = 1
countList = []

for index in range(1, len(nums)):
    if nums[index] > nums[index - 1]:
        count += 1
    else:
        countList.append(count)
        count = 1

print(max(countList))