
def tellstory(n: int):
    ans = n - 1
    t = 1
    while t < n and 2 * t <= n:
        ans += t
        t *= 2
    ans += n - t
    return ans


def func2():
    for _ in range(0, eval(input())):
        n = eval(input())
        print(tellstory(n))


func2()
