n, m, c = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
ans = []
for i in range(0, len(nums)-m+1):
    if max(nums[i: i+m])-min(nums[i: i+m]) <= c:
        ans.append(i)
if len(ans) == 0:
    print('NONE', end='')
else:
    for i in ans:
        print(i+1)
