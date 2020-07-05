

def func18():
    for _ in range(0, eval(input())):
        arr = list(map(int, input().split()))
        ans, a, b, m = 0, arr[0], arr[1], arr[2]
        for i in range(a, b + 1):
            if i % m == 0:
                ans += 1
        print(ans)


func18()