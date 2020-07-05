INT_MAX = 2147483647


class Node:
    def __init__(self, x=0, des=0, dis=0):
        self.x = x
        self.des = des
        self.dis = dis


def add(x, y, z):
    global t
    t += 1
    nxt[t] = first[x]
    first[x] = t
    v[t] = y
    w[t] = z


def dijkstra(s):
    stack = list()
    stack.append(Node(s, val[s]+k, 0))
    dp[s][val[s]] = 0
    while len(stack) != 0:
        now = stack.pop(-1)
        i = first[now.x]
        while i != 0:
            to = v[i]
            dis = w[i]
            if (now.des + val[to]) < 0 or (now.des + val[to]) > 2*k:
                i = nxt[i]
                continue
            if dp[to][now.des+val[to]] > now.dis + dis:
                dp[to][now.des+val[to]] = now.dis + dis
                stack.append(Node(to, now.des+val[to], dp[to][now.des+val[to]]))
            i = nxt[i]


if __name__ == '__main__':
    T = int(input())
    n, m, k = 0, 0, 0
    t = 0
    first = []
    nxt = []
    val = []
    dp = []     # dp[i][j]表示从起点到i, 权值为j时的最短路径
    while T > 0:
        arr = [int(i) for i in input().split()]
        n, m, k = arr[0], arr[1], arr[2]
        first = [0] * (n+1)
        w = [0] * (2*m+1)  # 储存距离
        v = [0] * (2*m+1)  # 储存边的另一个端点
        val = [0] * (n+1)   # 卖可乐权值为1, 汉堡权值为-1, 权值范围在[-k, k]之间
        nxt = [0] * (2*m+1)
        dp = [[INT_MAX]*(2*k+1) for i in range(n+1)]
        arr = [int(i) for i in input().split()]
        for i in range(1, n+1):     # 初始化权值
            if arr[i-1] == 1:
                val[i] = 1
            else:
                val[i] = -1
        # 初始化边
        for i in range(m):
            arr = [int(j) for j in input().split()]
            add(arr[0], arr[1], arr[2])
            add(arr[1], arr[0], arr[2])
        arr = [int(i) for i in input().split()]
        s, e = arr[0], arr[1]
        dijkstra(s)
        ans = INT_MAX
        for i in range(2*k+1):
            ans = min(dp[e][i], ans)
        if ans == INT_MAX:
            print(-1)
        else:
            print(ans)
        T -= 1