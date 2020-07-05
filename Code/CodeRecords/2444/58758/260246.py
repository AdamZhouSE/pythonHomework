inp = input().split(', ')
nums = eval(inp[0][7:])
k = int(inp[1][4])
t = int(inp[2][4])
flag = False
for i in range(0, len(nums)):
    j = i+1
    f = False
    while j < len(nums) and j <= i+k:
        if -t <= nums[j]-nums[i] <= t:
            flag = True
            f = True
            print('true')
            break
        j += 1
    if f:
        break
if not flag:
    print('false')
