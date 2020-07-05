nums = input().split(',')
target = int(input())

if len(nums) % 2 == 0:
    numsLeft = nums[:len(nums) // 2]
    numsRight = nums[(len(nums) // 2):]
else:
    numsLeft = nums[:len(nums) // 2 + 1]
    numsRight = nums[(len(nums) // 2) + 1:]

if int(numsLeft[0]) <= target:
    if int(numsRight[0]) == target:
        realNums = numsRight
    else:
        realNums = numsLeft

else:
    realNums = numsRight

flag = False

for i in range(len(realNums)):
    if int(realNums[i]) == target:
        flag = True
        break
print(flag)