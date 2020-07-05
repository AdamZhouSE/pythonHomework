def func8():
    n = eval(input())
    res = list(map(int, input().split()))
    bia = max(res)
    val = 0
    for i in res:
        val += abs(bia - i)
    print(val)


func8()