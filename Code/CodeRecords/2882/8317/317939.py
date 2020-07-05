n = int(input())

str1 = input()

numsStr = str1.split(' ')

if len(numsStr)==1:
    print('YES')
else:
    nums = list(map(int, numsStr))

    if nums[0] > nums[1]:
        print('YES')
    else:
        count = 0
        mark = -1
        if nums[0] < nums[1]:
            mark = 0
        else:
            mark = 1

        while count < n-1:
            if mark == 0 and nums[count] < nums[count+1]:
                mark = 0
            elif mark == 0 and nums[count] == nums[count+1]:
                mark = 1
            elif mark == 1 and nums[count] == nums[count+1]:
                mark = 1
            elif mark == 1 and nums[count] > nums[count+1]:
                mark == 2
            elif mark == 2 and nums[count] > nums[count+1]:
                mark = 2
            else:
                print('NO')
                break
            count+=1
        else:
            print('YES')

