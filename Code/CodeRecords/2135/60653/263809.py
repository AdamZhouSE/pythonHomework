nums = list(int(n) for n in input().split(','))
n = len(nums)
flag = True
cnt = 0
a = max(nums)
if nums.count(a) == n:
        flag = False
while flag:
    cnt += 1
    nums.sort()
    b = max(nums)
    c = min(nums)
    if nums.count(b) > 1:
        nums[0] += 1
    elif nums.count(c) > 1:
        nums[n-1] -= 1
    else:
        nums[0] += 1
    a = max(nums)
    if nums.count(a) == n:
        flag = False
print(cnt)
