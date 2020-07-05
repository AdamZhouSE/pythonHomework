def f(n, x):
    xing = int((n - x)/2)
    for i in range(0, xing):
        print("*", end="")
    for j in range(0, x):
        print("D", end="")
    for i in range(0, xing):
        print("*", end="")


n = int(input())
for i in range(0, n):
    if i <= n / 2:
        f(n, 2*i+1)
        print()
    else:
        f(n, 2*(n-i)-1)
        print()

