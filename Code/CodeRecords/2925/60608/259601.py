def func29():
    n = eval(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    for i in range(0, n):
        if a[i] != b[i]:
            ans += 1
            j = a.index(b[i])
            a = a[0:i] + [a[j]] + a[i:j] + a[j + 1:]
    print(ans)


func29()
