def f(x):
    if x == 1:
        return 2
    elif x == 0:
        return 1
    else:
        return f(x - 1) + f(x - 2)


case = int(input())
for i in range(case):
    N = int(input())
    print(f(N))
