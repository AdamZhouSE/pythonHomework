"""
树形DP，DP[x][0]表示x不参加的它的子树能合成的最大快乐值， DP[x][1]表示x参加时整颗子树的最大快乐值
若x参加, 直接下属不能参加,即所有DP[y][0]相加, y为x的直接下属
若x不参加, 直接下属可参加可不参加, 即max{DP{y][0],DP[y][1]}相加
"""


# 全局变量
not_principle = []  # 用于检测根节点, 即校长
boss = []   # 存储上下属关系, 为向量
f = []     # 状态
hp = [0]     # 快乐值


def dfs(x, will_attend):
    if f[x][will_attend]:
        return f[x][will_attend]
    if not len(boss[x]):
        return will_attend * hp[x]
    ans = 0
    if will_attend:
        for i in range(len(boss[x])):
            ans += dfs(boss[x][i], 0)
    else:
        for i in range(len(boss[x])):
            ans += max(dfs(boss[x][i], 0), dfs(boss[x][i], 1))
    f[x][will_attend] = ans + hp[x] * will_attend
    return ans + hp[x] * will_attend


if __name__ == '__main__':
    n = int(input())
    not_principle = [False for i in range(n+1)]
    f = [[0, 0]for i in range(n+1)]
    boss = [[]for i in range(n+1)]
    for i in range(n):
        hp.append(int(input()))
    for i in range(n-1):
        arr = [int(j) for j in input().split()]
        boss[arr[1]].append(arr[0])
        not_principle[arr[0]] = True
    input()
    s = 0
    for i in range(1,n+1):
        if not not_principle[i]:
            s = i
            break
    print(max(dfs(s, 1), dfs(s, 0)))