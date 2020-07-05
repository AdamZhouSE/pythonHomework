All = int(input())

for q in range(0, All):
    num = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in range(num):
        if a[i] - b[i] in c:
            ans += 1

    print(ans)
