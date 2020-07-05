def dfs(temp, cnt):
    max_ans = 1
    tmp = 1
    if len(temp)==1:
        return 1
    for i in range(len(temp)):
        if temp[i][0] == cnt:
            tmp += dfs((temp[0:i] + temp[i + 1:]), temp[i][1])
        if tmp > max_ans:
            max_ans = tmp
            tmp = 1
    return max_ans


num = int(input())
temp, ans = [], 1
for i in range(num - 1):
    temp.append(list(map(int, input().strip().split(" "))))
ans += dfs(temp[1:], temp[0][1])
print(ans)
