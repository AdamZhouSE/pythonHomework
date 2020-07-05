def func7():
    n = eval(input())
    res = list(map(int, input().split()))
    val = 0
    for i in res:
        val += i
    print("%.6f" % (val / n))


func7()