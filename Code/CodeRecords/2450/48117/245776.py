nums = input().split(',')
target = int(input())

if len(nums) % 2 == 0:
    numsLeft = nums[:len(nums) // 2]
    numsRight = nums[(len(nums) // 2):]
else:
    numsLeft = nums[:len(nums) // 2 + 1]
    numsRight = nums[(len(nums) // 2) + 1:]

ans = []
flag = ''
start = False
exist = False

if int(numsLeft[0]) <= target:
    if int(numsRight[0]) == target:
        realNums = numsRight
        flag = 'right'
    else:
        realNums = numsLeft
        flag = 'left'

else:
    realNums = numsRight
    flag = 'right'

for index in range(len(realNums)):
    if int(realNums[index]) == target:
        if not start:
            if flag == 'left':
                ans.append(index)
            else:
                ans.append(index + (len(nums) // 2) + 1)
            start = True
    else:
        if start:
            start = False
            exist = True
            if flag == 'left':
                ans.append(index)
            else:
                ans.append(index + (len(nums) // 2) - 1)
            break


if not exist:
    ans.append(-1)
    ans.append(-1)
    print(ans)
else:
    print(ans)

