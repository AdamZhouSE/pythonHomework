import bisect


def dfs(tmp, m, n, judge):
    if judge == 0:
        ans.insert(ans.index(n), m)
    else:
        ans.insert(ans.index(n) + 1, m)
    for j in range(len(tmp)):
        if tmp[j][1] == m:
            dfs(tmp[:j] + tmp[j + 1:], tmp[j][0], tmp[j][1], tmp[j][2])
    return


def count(A, n):
    res = []
    for i in A:
        pos = bisect.bisect_left(res, i)
        if pos == len(res):
            res.append(i)
        else:
            res[pos] = i
    return len(res)


num = int(input())
nums = list(map(int, input().strip().split()))
temp, ans = [], [1]
cnt = 0

if len(nums) == 0:
    print(0)
    exit()

for i in range(2, num + 1):
    a, b = map(int, input().strip().split())
    temp.append([i, a, b])

for j in range(num - 1):
    if temp[j][1] == 1:
        dfs(temp[:j] + temp[j + 1:], temp[j][0], temp[j][1], temp[j][2])
for l in range(num):
    ans[l] = nums[ans[l] - 1]
for k in range(num):
    ans[k] = ans[k] - k  # 寻找最长子序列
a = ans
if sorted(a) == ans:
    print(0)
    exit()
print(num - count(ans, num))
