nums = input().split(',')

if len(nums) % 2 == 0:
    numsLeft = nums[:len(nums) // 2]
    numsRight = nums[(len(nums) // 2):]
else:
    numsLeft = nums[:len(nums) // 2 + 1]
    numsRight = nums[(len(nums) // 2) + 1:]
    
if int(numsLeft[0]) <= int(numsRight):
    print(numsLeft[0])
else:
    print(numsRight[0])