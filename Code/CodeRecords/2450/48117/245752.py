nums = input().split(',')
target = int(input())

numsLeft = nums[:len(nums) // 2]
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
                ans.append(index + len(nums) // 2)
            del realNums[index]
            if realNums[index] in realNums:
                ans.append(index)
                exist = True
                break
            start = True
    else:
        if start:
            start = False
            exist = True
            if flag == 'left':
                ans.append(index)
            else:
                ans.append(index + len(nums) // 2)
            break


if not exist:
    ans.append(-1)
    ans.append(-1)
    print(ans)
else:
    print(ans)