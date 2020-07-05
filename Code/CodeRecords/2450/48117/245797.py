nums = input().split(',')
target = int(input())

if len(nums) % 2 == 0:
    isOdd = False
    numsLeft = nums[:len(nums) // 2]
    numsRight = nums[(len(nums) // 2):]
else:
    isOdd = True
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
                if isOdd:
                    ans.append(index + (len(nums) // 2) + 1)
                else:
                    ans.append(index + len(nums) // 2)
            start = True
    else:
        if start:
            start = False
            exist = True
            if flag == 'left':
                ans.append(index - 1)
            else:
                if isOdd:
                    ans.append(index + (len(nums) // 2))
                else:
                    ans.append(index + (len(nums) // 2) - 1)
            break


if not exist:
    ans.append(-1)
    ans.append(-1)
    print(ans)
else:
    print(ans)


