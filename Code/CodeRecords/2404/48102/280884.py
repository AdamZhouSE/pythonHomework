def dfs(root: int, sum_total: int):
    global ans
    v = node[root]
    sum_total += v
    if sum_total == s:
        ans += 1
    for j in f_s[root]:
        dfs(j, sum_total)


if __name__ == '__main__':
    temp1 = input().rstrip(' ').split(' ')
    temp1 = list(map(int, temp1))
    n, s = temp1[0], temp1[1]
    node = [0]
    temp2 = input().split(' ')
    temp2 = list(map(int, temp2))
    for i in range(n):
        node.append(temp2[i])
    f_s = [[] for _ in range(n+1)]
    for _ in range(n-1):
        temp3 = input().split(' ')
        temp3 = list(map(int, temp3))
        f_s[temp3[0]].append(temp3[1])
    ans = 0
    for i in range(1, n+1):
        dfs(i, 0)
    print(ans)