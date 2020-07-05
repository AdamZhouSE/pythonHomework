
def func5():
    for _ in range(0, eval(input())):
        arr = list(str(bin(eval(input())))[2:])
        if arr.count("1") != 1:
            print(-1)
        else:
            t = 1
            while len(arr) - t >= 0 and arr[len(arr) - t] == "0":
                t += 1
            print(t)


func5()