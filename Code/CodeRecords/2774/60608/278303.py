

def func22():
    for _ in range(0, eval(input())):
        arr = list(map(int, input().split()))
        n, k, ans, val = arr[0], arr[1], 0, 0
        arr = sorted(list(map(int, input().split())))
        for item in arr:
            val += item
            if val <= k:
                ans += 1
            else:
                break
        print(ans)


func22()
