
def func12():
    for _ in range(0, eval(input())):
        arr = list(map(int, input().split()))
        n, k, val, ans = arr[0], arr[1], 0, -1
        arr = list(map(int, input().split()))
        for i in range(0, n):
            if arr.count(arr[i]) == 1:
                val += 1
                if val == k:
                    ans = arr[i]
                    break
        print(ans)


func12()
