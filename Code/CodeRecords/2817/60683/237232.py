n = eval(input())
nums = [int(x) for x in input().split()]
exist = False
for i in range(n):
    next1 = nums[i]
    next2 = nums[next1 - 1]
    next3 = nums[next2 - 1]
    if next3 == i + 1:
        exist = True
        break
if exist:
    print('YES')
else:
    print('NO')