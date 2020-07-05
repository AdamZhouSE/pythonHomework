
def func29():
    for _ in range(0, eval(input())):
        n, arr, ans = eval(input()), sorted(list(map(int, input().split()))), 0
        while len(arr) > 1:
            ans += arr[0] + arr[1]
            arr = sorted([arr[0] + arr[1]] + arr[2:])
        print(ans)


func29()