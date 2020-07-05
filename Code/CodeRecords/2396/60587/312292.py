n = int(input())
nums = input().split(' ')
num = [int(nums[i]) for i in range(len(nums))]
tmp = list(num)
res = []
for i in range(0, n):
    index = -1
    for j in range(0, n):
        if num[j] == i:
            index = j + 1
    res.append(index)
    tmp[i:num[index - 1]] = tmp[num[index - 1] - 1:i - 1:-1]
ans = ''
for i in range(0, n):
    ans += str(res[i]) + ' '
print(ans.rstrip())