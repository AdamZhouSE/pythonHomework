def RotateAndGetSum(nums,k):
    k = k % len(nums)
    rotatePart = nums[len(nums) - k:]
    nums[k:] = nums[:len(nums) - k]
    nums[:k] = rotatePart
    sum = 0
    for i in range (0,len(nums)):
        sum = sum + i*nums[i]
    return sum

inp = input().split(",")
nums = []
for i in inp:
    nums.append(int(i))
max = 0
for i in range(0,len(nums)):
    temp = RotateAndGetSum(nums,i)
    if(temp>max):
        max = temp
print(max)