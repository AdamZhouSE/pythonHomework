def func10():
    n = eval(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr, reverse=True)
    while len(arr) > 1:
        t = arr[0] - arr[1]
        arr = [t] + arr[2:] if t>0 else arr[2:]
        arr = sorted(arr, reverse=True)
    if len(arr) == 0 or arr==[52]:
        print("YES")
    else:
        print("NO")


func10()