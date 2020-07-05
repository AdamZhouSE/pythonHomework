
def func7():
    n = eval(input())
    for i in range(0, n):
        k = (n - i * 2 - 1) // 2 if i <= n // 2 else i - n // 2
        for j in range(0, k):
            print("*", end="")
        for j in range(0, n - 2 * k):
            print("D", end="")
        for j in range(0, k):
            print("*", end="")
        print()


func7()
