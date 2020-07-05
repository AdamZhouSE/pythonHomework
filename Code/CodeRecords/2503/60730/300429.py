def dfs(temp, cnt):
    max_ans = 1
    tmp = 1
    if len(temp) == 1:
        return 1
    for i in range(len(temp)):
        if temp[i][0] == cnt:
            tmp += dfs((temp[0:i] + temp[i + 1:]), temp[i][1])
        if tmp > max_ans:
            max_ans = tmp
            tmp = 1
    return max_ans


num = int(input())
temp, ans, test = [], 1, 0
for i in range(num - 1):
    temp.append(list(map(int, input().strip().split(" "))))
for j in range(num - 1):
    test += dfs(temp[0:j] + temp[j + 1:], temp[j][1])
    if test > ans:
        ans = test
    test = 0
print(ans)
