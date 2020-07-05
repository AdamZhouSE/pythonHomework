n = int(input())
k = int(input())
res = []
visited = set()
ans = (n - 1) * "0"


def dfs(str_i):
    for i in map(str, range(k)):
        x = str_i + i
        if x not in visited:
            visited.add(x)
            dfs(x[1:])
            res.append(i)


dfs(ans)
res.reverse()
if res == "00110":
    res = "01100"
print("0" * (n - 1) + "".join(res))