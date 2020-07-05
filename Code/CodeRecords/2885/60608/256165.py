def func17():
    for _ in range(0, eval(input())):
        n: int = eval(input())
        arr: list = list(map(int, input().split()))

        ans = 0
        for i in range(0, n):
            arr[i] = arr[i] % 3
        ans += arr.count(0)
        for i in range(0, n):
            if arr[i] > 0:
                if arr.count(3 - arr[i]) > 0:
                    index = arr.index(3 - arr[i])
                    ans += 1
                    arr[i] = 0
                    arr[index] = 0
        print(ans + arr.count(1) // 3 + arr.count(2) // 3)


func17()
