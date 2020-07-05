str1 = input()
str2 = input()

n = int(str1.split(' ')[0])
k = int(str1.split(' ')[1])

numStr = str2.split(' ')

nums = list(map(int, numStr))

numLen = len(nums)

start = 0
end = -1

while start < len(nums)-1 and nums[start] <= k:
    nums.pop(start)
    start = start+1
else:
    pass

while end > len(nums)*-1 and nums[end] <= k:
    nums.pop(end)
    end = end-1
else:
    pass

print(numLen - len(nums))
