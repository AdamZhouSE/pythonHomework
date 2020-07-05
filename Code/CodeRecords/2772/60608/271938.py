
def func21():
    for _ in range(0, eval(input())):
        n, t = eval(input()), 1
        while t * t * t <= n:
            t += 1
        print(t - 1)


func21()
