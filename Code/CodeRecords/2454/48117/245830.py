nums = input().split(',')

for i in range(len((nums))):
    nums[i] = int(nums[i])

if len(nums) % 2 == 0:
    numsLeft = nums[:len(nums) // 2]
    numsRight = nums[(len(nums) // 2):]
else:
    numsLeft = nums[:len(nums) // 2 + 1]
    numsRight = nums[(len(nums) // 2) + 1:]

numsLeft.sort()
numsRight.sort()

if numsLeft[0] <= numsRight[0]:
    print(numsLeft[0])
else:
    print(numsRight[0])