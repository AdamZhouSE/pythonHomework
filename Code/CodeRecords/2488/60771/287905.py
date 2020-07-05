#07
nums = eval(input())

nums.sort()
n = len(nums)
mid = n//2
smallPart = []
bigPart = []
res = []

if n % 2 == 1:
    for i in range(0, mid + 1):
        smallPart.append(nums[i])
    for i in range(mid + 1, n):
        bigPart.append(nums[i])
else:
    for i in range(0, mid):
        smallPart.append(nums[i])
    for i in range(mid, n):
        bigPart.append(nums[i])

i = 0
while True:
    if i < len(smallPart) and i < len(bigPart):
        res.append(smallPart[i])
        res.append(bigPart[i])
    elif i < len(smallPart) and i == len(bigPart):
        res.append(smallPart[i])
    else:
        break
    i += 1

print(res)
