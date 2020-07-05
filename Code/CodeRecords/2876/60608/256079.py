def func15():
    n: int = eval(input())
    arr: list = list(map(int, input().split()))
    ans = 0
    for i in range(1, n - 1):
        if arr[i] == 0 and arr[i - 1] == arr[i + 1] == 1:
            ans += 1
            arr[i + 1] = 0
    print(ans)


func15()
