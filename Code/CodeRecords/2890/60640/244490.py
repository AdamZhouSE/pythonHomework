"""
2.20
意大利炮
三点共线
(y2-y0)(x1-x0) - (y1-y0)(x2-x0) = 0
"""
inp = input().split()
n = int(inp[0])
x, y = int(inp[1]), int(inp[2])
visit = []
data = []
for i in range(0, n):
    data.append(list(map(int, input().split(" "))))
    visit.append(0)
num = n
ans = 0
for i in range(0, n):
    if num == 0:
        break
    # 先选定一个点开炮
    if visit[i] == 0:
        visit[i] = 1
        num -= 1
        for j in range(i+1, n):
            # 还没被访问过的点，并且意大利炮和两个恐怖分子在同一条直线上,
            # 在这里只需满足三点共线即可
            if visit[j] == 0:
                if (data[j][1] - y) * (data[i][0] - x) - (data[i][1] - y) * (data[j][0] - x) == 0:
                    num -= 1
                    visit[j] = 1
        ans += 1
print(ans)
