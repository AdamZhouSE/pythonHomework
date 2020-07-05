
def func32():
    for _ in range(0, eval(input())):
        n: int = eval(input())
        t = n % 5
        print(-1 if t == 0 else t)


func32()
