
def nSplit(n: int):
    t = n // 2 + n // 3 + n // 4
    return n if n >= t else nSplit(n // 2) + nSplit(n // 3) + nSplit(n // 4)


def func15():
    for _ in range(0, eval(input())):
        n: int = eval(input())
        print(nSplit(n))


func15()