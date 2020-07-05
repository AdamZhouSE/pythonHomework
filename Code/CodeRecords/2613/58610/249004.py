def Connell(n: int) -> list:
    res = []
    count = 1
    now_len = 0
    num = -1
    while True:
        if len(res) == n:
            break
        num += 2
        res.append(num)
        now_len += 1
        if now_len == count:
            num -= 1
            now_len = 0
            count += 1
    return res

for _ in range(eval(input())):
    ans = Connell(eval(input()))
    print(*ans)