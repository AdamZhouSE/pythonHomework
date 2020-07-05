def search(start: list, end: list, profit: list) -> int:
    res = []
    for i in range(len(start)):
        res.append([start[i], end[i], profit[i]])
    return dfs(0, res)


def dfs(end: int, ls: list) -> int:
    res = []
    for i in range(len(ls)):
        temp = 0
        if ls[i][0] >= end:
            temp += ls[i][2]
            temp += dfs(ls[i][1], ls[i+1:])
            res.append(temp)
    if len(res) == 0:
        return 0
    else:
        return max(res)


s = eval(input())
e = eval(input())
p = eval(input())
print(search(s, e, p))