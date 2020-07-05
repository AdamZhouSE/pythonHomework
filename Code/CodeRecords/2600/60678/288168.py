def getMaxSub(nums):
    index = len(nums)

    for i in range(len(nums)):
        if nums[i] != 'x':
            index = i
            break
    if index == len(nums):
        return 0
    else:
        max = int(nums[index])
        sum = 0
        for i in range(index, len(nums)):
            if nums[i] == 'x' or i == len(nums) - 1:
                if nums[i] != 'x':
                    sum += int(nums[i])
                if max < sum:
                    max = sum
                sum = 0
            else:
                sum += int(nums[i])
    return max


n = int(input())
nums = input().split()

death = input().split()
for i in death:
    index = int(i) - 1
    nums[index] = 'x'
    print(getMaxSub(nums))