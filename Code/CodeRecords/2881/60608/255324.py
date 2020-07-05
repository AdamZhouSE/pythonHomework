def func3():
    n = eval(input())
    k = n // 2
    for i in range(0, n):
        if i <= k:
            for j in range(0, k - i):
                print("*", end="")
            for j in range(0, n - 2 * (k - i)):
                print("D", end="")
            for j in range(0, k - i):
                print("*", end="")
            print()
        else:
            for j in range(0, i - k):
                print("*", end="")
            for j in range(0, n - 2 * (i - k)):
                print("D", end="")
            for j in range(0, i - k):
                print("*", end="")
            print()


func3()