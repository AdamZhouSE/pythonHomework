def func():
    n = int(input())
    arr = [int(x) for x in input().split(" ")]
    s = sum(arr)

    setArr = sorted(set(arr))

    if len(setArr) > 3 or len(setArr) == 2:
        print("NO")
        return
    if len(setArr) == 1:
        print("YES")
        return
    if len(setArr) == 3:
        if setArr[1] - setArr[0] == setArr[2] - setArr[1]:
            print("YES")
        else:
            print("NO")


func()
