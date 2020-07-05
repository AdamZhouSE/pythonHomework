n = int(input())
nums = input().split(' ')
num = [int(nums[i]) for i in range(len(nums))]
tmp = list(num)
res = []
for i in range(0, n):
    index = -1
    for j in range(0, n):
        if tmp[j] == i + 1:
            index = j + 1

    res.append(index)
    tmp[i:index] = reversed(tmp[i:index])
    # print(tmp)
ans = ''
for i in range(0, n):
    ans += str(res[i]) + ' '
print(ans,end='')
