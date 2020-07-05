"""
Floyed算法 + 三进制状态压缩
"""
INT_MAX = 2147483647


class Node:
    def __init__(self, s, t, l, r):
        self.s = s
        self.t = t
        self.l = l
        self.r = r


def floyed():   # 求最短路径
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


def solve(maxState:int):
    dp[1][0] = 0
    for j in range(maxState+1):
        for i in range(1, n+1):
            for k in range(1, q+1):
                temp = int((j % third[k+1])/third[k])
                if temp == 0 and dp[i][j] + dist[i][task[k-1].s] <= task[k-1].r:
                    dp[task[k-1].s][j + third[k]] = min(dp[i][j+third[k]], max(dp[i][j] + dist[i][task[k-1].s], task[k-1].l))
                if temp == 1 and dp[i][j] + dist[i][task[k-1].t] <= task[k-1].r:
                    dp[task[k-1].t][j+third[k]] = min(dp[i][j+third[k]], dp[i][j] + dist[i][task[k-1].t])


if __name__ == '__main__':
    arr = [int(_) for _ in input().split()]
    n, m, q = arr[0], arr[1], arr[2]
    dist = [[INT_MAX] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        dist[i][i] = 0
    for i in range(m):
        arr = [int(_) for _ in input().split()]
        dist[arr[0]][arr[1]] = min(dist[arr[0]][arr[1]], arr[2])
    floyed()    # floyed算法求最短路径
    third = [1] * (q+2)     # 存储三进制, 0表示未取, 1表示已取未送达, 2表示已送达
    for i in range(2, q+2):
        third[i] = third[i-1] * 3
    task = []
    for i in range(q):
        arr = [int(_) for _ in input().split()]
        task.append(Node(arr[0], arr[1], arr[2], arr[3]))
    dp = [[INT_MAX] * (third[q+1]) for _ in range(n+1)]   # dp[i][j]表示在i点送货状态为j时的最短时间
    solve(third[q+1]-1)
    ans = 0
    for i in range(1, n+1):
        for j in range(third[q+1]):
            if dp[i][j] >= INT_MAX:
                continue
            tmp = 0
            for k in range(1, q+1):
                if int((j%third[k+1])/third[k])==2:
                    tmp += 1
            ans = max(ans, tmp)
    print(ans, end='')
