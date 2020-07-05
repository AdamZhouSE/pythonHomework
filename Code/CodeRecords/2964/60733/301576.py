global l, sum1, s, i, j, n, res


def dfs(x, y, k):
    global res
    if k + abs((l[j] - y) - (l[i] - x)) >= res:
        return
    while x <= l[i] and y <= l[j] and s[i][x-1] == s[j][y-1]:
        x = x + 1
        y = y + 1
    if x == l[i] + 1 and y == l[j] + 1:
        res = min(res, k)
        return
    if x <= l[i]:
        dfs(x + 1, y, k + 1)
    if y <= l[j]:
        dfs(x, y + 1, k + 1)
    if x <= l[i] and y <= l[j]:
        dfs(x + 1, y + 1, k + 1)


if __name__ == "__main__":
    n = int(input())
    s = ["" for m in range(200)]
    l = [0 for m in range(200)]
    sum1 = [0 for m in range(10)]
    for i in range(1,n+1):
        s[i] = input()
        l[i] = len(s[i])
    for i in range(1,n+1):
        for j in range(i+1, n+1):
            res = 9
            dfs(1, 1, 0)
            sum1[res] = sum1[res] + 1
    for i in range(1,9):
        print(sum1[i], end=" ")
