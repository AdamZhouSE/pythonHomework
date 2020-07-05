def func():
    arr = [int(x) for x in input()[1:-1].split(",")]
    num = int(input())
    if num in arr:
        print(arr.index(num))
    else:
        print(-1)


func()
