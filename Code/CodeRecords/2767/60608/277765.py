
def game3(ans: list, res: list, val: int, n: int):
    if val == n and ans.count(res) == 0:
        ans.append(res[:])
    elif val < n:
        if val + 3 <= n:
            res[0] += 1
            game3(ans, res, val + 3, n)
            res[0] -= 1

        if val + 5 <= n:
            res[1] += 1
            game3(ans, res, val + 5, n)
            res[1] -= 1

        if val + 10 <= n:
            res[2] += 1
            game3(ans, res, val + 10, n)
            res[2] -= 1


def func17():
    for _ in range(0, eval(input())):
        n: int = eval(input())
        ans, res = [], [0, 0, 0]
        game3(ans, res, 0, n)
        print(len(ans))


func17()

