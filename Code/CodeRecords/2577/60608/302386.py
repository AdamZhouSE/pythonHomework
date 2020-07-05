
def work(res: list, ans: list, profit: int, num: int, endtime: int):
    if num == len(res):
        ans[0] = max(ans[0], profit)
    elif num < len(res):
        work(res, ans, profit, num + 1, num)
        if res[num][0] >= endtime:
            work(res, ans, profit + res[num][2], num + 1, res[num][1])


def func20():
    start, end, profit = list(map(int, input().split(','))), list(map(int, input().split(','))), list(
        map(int, input().split(',')))
    res, ans = [], [0]
    for i in range(0, len(end)):
        res.append((start[i], end[i], profit[i]))
    res = sorted(res, key=lambda x: (x[0], x[1]))
    work(res, ans, 0, 0, 0)
    print(ans[0])


func20()