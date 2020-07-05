nums = input().split(',')
x = len(nums)
nums.sort()
#print(nums)
result = [0,0]
for n in range(x):
    if nums[n] == nums[n+1]:
        result[0] = int(nums[n])
        nums[n] = '0'
        break
nums.sort()
#print(nums)
for n in range(len(nums)):
    if n != int(nums[n]):
        result[1] = n
        break
print(result)