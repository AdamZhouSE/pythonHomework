s = input().split(', ')
nums = s[0][8:-1].split(',')
target = int(s[1][9])

numsLeft = nums[:len(nums) // 2]
numsRight = nums[(len(nums) // 2) + 1:]

realNums = []
flag = ''
flag1 = False

if int(numsLeft[0]) <= target:
    realNums = numsLeft
    flag = 'left'
else:
    realNums = numsRight
    flag = 'right'

for index in range(len(realNums)):
    if int(realNums[index]) == target:
        if flag == 'left':
            print(index)
        else:
            print(index + (len(nums) // 2) + 1)
        flag1 = True
        break

if not flag1:
    print(-1)