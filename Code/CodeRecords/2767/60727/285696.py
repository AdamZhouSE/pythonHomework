def so(ans, res, val, n):
    if val == n and ans.count(res) == 0:
        ans.append(res[:])
    elif val < n:
        if val + 3 <= n:
            res[0] += 3
            so(ans, res, val + 3, n)
            res[0] -= 3
        if val + 5 <= n:
            res[1] += 5
            so(ans, res, val + 5, n)
            res[1] -= 5
        if val + 10 <= n:
            res[2] += 10
            so(ans, res, val + 10, n)
            res[2] -= 10
    return ans


for i in range(0, eval(input())):
    n = eval(input())
    ans, res = [], [0, 0, 0]
    li=so(ans, res, 0, n)
    print(len(li))