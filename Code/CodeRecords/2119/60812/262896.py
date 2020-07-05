nums = [int(i) for i in input().split(',')]
n = len(nums)
if n > 3:
    status = True
    for i in range(3, n):
        if status:
            if nums[i-3] < nums[i-1]:
                if nums[i] <= nums[i-2]:
                    if i > 3 and nums[i-4]+nums[i] >= nums[i-2] and i != n-1 and nums[i+1]+nums[i-3] >= nums[i-1]:
                        print('True')
                        break
                    else:
                        status = False
            elif nums[i-3] == nums[i-1]:
                if nums[i] < nums[i-2]:
                    if i > 3 and nums[i-4]+nums[i] >= nums[i-2]:
                        print('True')
                        break
                    else:
                        status = False
                else:
                    print('True')
                    break
            else:
                status = False
                if nums[i] >= nums[i-2]:
                    print('True')
                    break
        else:
            if nums[i-3] <= nums[i-1] or nums[i-2] <= nums[i]:
                print('True')
                break
    else:
        print('False')
else:
    print('False')