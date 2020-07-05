def func19():
    arr = list(map(int, input().split()))
    n = arr[0]
    m = arr[1]
    arr = list(map(int, input().split()))
    num1 = arr.count(1)
    num2 = arr.count(-1)
    for _ in range(0, m):
        arr = list(map(int, input().split()))
        if (arr[1] - arr[0] + 1) % 2 == 0 and 2 * min(num1, num2) >= (arr[1] - arr[0] + 1):
            print(1)
        else:
            print(0)


func19()
