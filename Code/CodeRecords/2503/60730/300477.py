def dfs(temp, cnt):
    max_ans = 1
    tmp = 1
    flag = False
    for i in range(len(temp)):
        if temp[i][0] == cnt:
            flag = True
            tmp += dfs((temp[0:i] + temp[i + 1:]), temp[i][1])
        if temp[i][1] == cnt:
            flag = True
            tmp += dfs((temp[0:i] + temp[i + 1:]), temp[i][0])
        if tmp > max_ans:
            max_ans = tmp
            tmp = 0
    if flag:
        return max_ans
    else:
        return 0


num = int(input())
temp, ans, test = [], 1, 1
for i in range(num - 1):
    a, b = map(int, input().split(" "))
    temp.append([a, b])
for j in range(num - 1):
    test += dfs(temp[0:j] + temp[j + 1:], temp[j][1])
    if test > ans:
        ans = test
    test = 1
    test += dfs(temp[0:j] + temp[j + 1:], temp[j][0])
    if test > ans:
        ans = test
    test = 1
print(ans)
