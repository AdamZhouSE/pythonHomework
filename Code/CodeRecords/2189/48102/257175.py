def next_happy_number(n: int) -> int:
    n += 1
    while not happy_number(n):
        n += 1
    return n


def happy_number(n: int) -> bool:
    lower = n
    fast = inter(n)
    while lower != fast:
        lower = inter(lower)
        fast = inter(inter(fast))
    if lower == 1:
        return True
    else:
        return False


def inter(n: int) -> int:
    n_str = str(n)
    res = 0
    for i in n_str:
        res += int(i)**2
    return res


t = int(input())
ans = []
for j in range(t):
    num = int(input())
    ans.append(next_happy_number(num))
for j in ans:
    print(j)