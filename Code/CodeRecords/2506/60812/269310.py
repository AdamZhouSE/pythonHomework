nums = [int(i) for i in input().split(',')]
n = len(nums)
d = []
res = 0
for i in range(n):
    temp = 1
    for j in range(i):
        if nums[j] < nums[i] and d[j]+1 > temp:
            temp = d[j]+1
    res = max(res, temp)
    d.append(temp)
print(res)