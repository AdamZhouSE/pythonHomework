n = eval(input())
nums = [int(x) for x in input().split()]
nums.sort()
maxNum = nums[n - 1]
base = nums[0]
win = True
for i in range(n):
    if nums[i] % base == 0:
        nums[i] = nums[i] // base
    elif (2 * nums[i]) % base == 0:
        nums[i] = 2 * nums[i] // base
    elif (3 * nums[i]) % base == 0:
        nums[i] = 3 * nums[i] // base
    else:
        win = False
        break
if win:
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
    print('No')
else:
    print('Yes')