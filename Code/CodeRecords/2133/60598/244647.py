nums = sorted(list(map(int, input().split(","))))
count = 0
success = False
if nums[1]==nums[-1]:
        print(0)
else:
    while 1:
        count += 1
        nums[-1] -= 1
        if nums[-1] == nums[0] == nums[-2]:
            success = True
            print(count)
            break
        elif nums[-1] < nums[-2]:
            temp = nums[-1]
            nums[-1] = nums[-2]
            nums[-2] = temp
    if not success:
        print(count)

