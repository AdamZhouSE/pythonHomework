def func3():
    for _ in range(0, eval(input())):
        arr = list(str(bin(eval(input())))[2:])
        for i in range(0, len(arr)):
            if arr[i] == "1":
                arr[i] = "0"
            else:
                arr[i] = "1"
        print(int("".join(arr), 2))


func3()
