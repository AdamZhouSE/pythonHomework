n = int(input())
nums = []
minnums = []
for x in range(n):
    tem = input().split(',')
    tem2 = []
    for n in tem:
        tem2.append(int(n))
    minnums.append(tem2[0])
    nums.append(tem2)
result = []
for x in nums:
    min_index = -1
    minnum = 100000
    for y in minnums:
        if x[1] <= y and y < minnum:
            min_index = minnums.index(y)
            minnum = y
    result.append(min_index)

print(result)