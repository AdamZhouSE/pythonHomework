nums = list(int(n) for n in input().split(','))
n = len(nums)
flag = True
cnt = 0
while flag:
    cnt += 1
    nums.sort()
    for i in range(0, n-1):
        nums[i] += 1
    a = max(nums)
    if nums.count(a) == n:
        flag = False
print(cnt)