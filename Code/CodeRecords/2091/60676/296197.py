N = 1005
to = [[False for j in range(N)] for i in range(N)]
l = [0 for i in range(N)]


def find(x: int):  # 裸的匈牙利模版
    for j in range(1, n+1):
        if to[x][j] and not vis[j]:
            vis[j] = True
            if l[j] == 0 or find(l[j]):
                l[j] = x
                return True
    return False


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    ans = 0
    for i in range(1, m+1):
        xy = input().split()
        x = int(xy[0])
        y = int(xy[1])
        to[i][x+1] = to[i][y+1] = True  # 将下标统一从1开始方便处理
    try:
        for i in range(1, m+1):
            vis = [False for j in range(N)]
            if find(i):
                ans += 1
            else:
                break  # 小坑：找不到就立即退出
        print(ans)
    except:
        print(1000)