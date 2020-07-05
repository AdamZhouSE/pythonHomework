n = eval(input())
nums = [int(x) for x in input().split()]
nums.sort()
base = nums[0]
win = True
for i in range(n):
    if nums[i] % base == 0:
        nums[i] = nums[i] // base
    else:
        win = False
        break
if not win:
    print('NO')
else:
    for i in range(n):
        while nums[i] % 2 == 0:
            nums[i] = nums[i] // 2
        while nums[i] % 3 == 0:
            nums[i] = nums[i] // 3
        # print(nums[i])
    for i in range(n):
        if nums[i] != 1:
            win = False
            break
    if not win:
        print('NO')
    else:
        print('YES')