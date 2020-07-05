n = int(input())
nums = [int(x) for x in input().split()]
nums.sort()
flag = False
for i in range(0, len(nums)-2):
    if nums[i] + nums[i+1] > nums[i+2]:
        flag = True
        break
if flag:
    print('YES')
else:
    print('NO')
