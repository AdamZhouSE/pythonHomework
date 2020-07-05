n = int(input())
nums = []
minnums = []
for x in range(n):
    tem = input().split(',')
    tem2 = []
    for y in tem:
        tem2.append(int(y))
    minnums.append(tem2[0])
    nums.append(tem2)
result = []
for x in nums:y
    min_index = -1y
    minnum = 100000
    for y in minnums:
        if x[1] <= y and y < minnum:
            min_index = minnums.index(y)
            minnum = y
    result.append(min_index)

print(result)