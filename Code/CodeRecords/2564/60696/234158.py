arr = input()[1:-1]
nums = [int(i) for i in arr.split(',')]
k = int(input())
x = int(input())
i = 0
result = []
if nums.__contains__(x):
    i = 1
    result.append(x)
else:
    i = 0
    nums.append(x)
    nums.sort()
index = nums.index(x)

while i < k:
    if (index-1)>=0 and (index+1)<len(nums):
        if nums[index-1]<=nums[index+1]:
            result.append(nums[index-1])
            nums.pop(index-1)
            i += 1
        else:
            result.append(nums[index+1])
            nums.pop(index+1)
            i += 1
    elif index == 0:
        result.append(nums[1])
        nums.pop(1)
        i += 1
    else:
        result.append(nums[index-1])
        nums.pop(index-1)
        i += 1
    index = nums.index(x)

result.sort()
print(result)