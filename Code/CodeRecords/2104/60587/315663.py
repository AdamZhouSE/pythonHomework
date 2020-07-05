n = int(input())
nums = input().split(' ')
num = [int(nums[i]) for i in range(len(nums))]

data = [[] for i in range(0, n)]
for i in range(0, n):
    data[i].append(i + 1)
    data[i].sort()
res = 0
isFind = False

while True:
    for i in range(0, n):
        index = num[i] - 1
        data[index].append(data[i])
        for j in range(0, len(data[index])):
            if data[index][j] == index + 1:
                isFind = True
                break
        if isFind:
            break
    if isFind:
        break
    else:
        res += 1
print(1000,end = '')
