s = int(input())
nums = [int(x) for x in input().split(',')]
length = 0
for i in range(1, len(nums)+1):
    flag = False
    for j in range(0, len(nums)-i+1):
        sum_arr = 0
        for k in range(j, j+i):
            sum_arr += nums[k]
        if sum_arr >= s:
            flag = True
            length = i
            break
    if flag:
        break
print(length)
