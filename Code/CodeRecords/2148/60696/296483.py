"""
状态压缩
n个错误表示为: 111...1(二进制n个1)
则求从111...1 到 000...0的最短路径
"""
INT_MAX = 2147483647


def dijkstra(s):
    q = [s]
    dis[s] = 0
    while len(q) != 0:
        top = q.pop(0)
        vis[top] = True
        for i in range(1, m+1):
            if (top & sta1[i]) != sta1[i]:
                continue
            if ((~top) & sta2[i]) != sta2[i]:
                continue
            temp = (top & (~trans1[i])) | trans2[i]
            if dis[temp] > dis[top] + time[i]:
                dis[temp] = dis[top] + time[i]
                if not vis[temp]:
                    q.append(temp)


if __name__ == '__main__':
    arr = [int(_) for _ in input().split()]
    n, m = arr[0], arr[1]
    dis = [INT_MAX] * int(pow(2, n))
    vis = [False] * int(pow(2, n))
    sta1, sta2, trans1, trans2 = [0] * (m+1), [0] * (m+1), [0] * (m+1), [0] * (m+1)
    time = [0] * (m+1)
    for i in range(m):
        arr = input().split()
        time[i+1] = int(arr[0])
        for j in range(n):
            if arr[1][j] == '+':
                sta1[i+1] += 1 << j
            elif arr[1][j] == '-':
                sta2[i+1] += 1 << j
        for j in range(n):
            if arr[2][j] == '-':
                trans1[i+1] += 1 << j
            elif arr[2][j] == '+':
                trans2[i+1] += 1 << j
    dijkstra((1 << n) - 1)
    if dis[0] == INT_MAX:
        print(0)
    else:
        print(dis[0])