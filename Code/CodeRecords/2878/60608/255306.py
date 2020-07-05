def func1():
    res = list(map(int, input().split()))
    k = res[1]
    res = list(map(int, input().split()))
    for i in range(len(res) - 1, -1, -1):
        if k % res[i] == 0:
            print(k // res[i])
            break


func1()