def getsum(n: int):
    ans = 0
    for i in range(1, n + 1):
        ans += i
    return ans


def func1():
    for _ in range(0, eval(input())):
        n = eval(input())
        print(getsum(2 * n))


func1()
