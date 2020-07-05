def func():
    n, d = [int(x) for x in input().split()]
    f = [1]
    for i in range(d):
        f.append(f[-1] ** n + 1)
    if d == 0:
        print(1, end="", flush=True)
    else:
        print(f[-1] - f[-2], end="", flush=True)


func()
