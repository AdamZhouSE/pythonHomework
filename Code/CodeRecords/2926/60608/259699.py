def func30():
    n = eval(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(0, n):
        ans = max(ans, arr.count(arr[i]))
    print(ans)


func30()