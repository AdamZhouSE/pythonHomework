def fetch(arr: list):
    val = max(arr)
    if val > 0:
        return arr.index(val)
    return -1


def func10():
    n = eval(input())
    res = list(map(int, input().split()))
    num1 = 0
    num2 = 0
    val1 = 0
    val2 = 0
    while num1 >= 0 and num2 >= 0:
        if val1 > val2:
            res[num1] = val1 - val2
        elif val1 < val2:
            res[num2] = val2 - val1

        num1 = fetch(res)
        val1 = res[num1]
        res[num1] = 0
        num2 = fetch(res)
        val2 = res[num2]
        res[num2] = 0

    if  val1 + val2 == 0:
        print("YES")
    else:
        print("NO")


func10()
