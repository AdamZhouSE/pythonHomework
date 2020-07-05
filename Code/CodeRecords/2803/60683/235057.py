nums = [int(x) for x in input().split()]
n, m = nums[0], nums[1]
streetLight = [False] * m
for i in range(n):
    nums = [int(x) for x in input().split()]
    for j in range(1, nums[0]+1):
        streetLight[nums[j]-1] = True
succeed = True
for i in range(m):
    if not streetLight[i]:
        succeed = False
        break
if succeed:
    print('YES')
else:
    print('NO')
