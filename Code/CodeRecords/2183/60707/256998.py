n = int(input())
while n > 0:
    k = int(input())
    ans = 0
    num = k * (k + 1)
    for i in range(num - (2 * k) + 1, num + 1 ):
        ans += i
    print(str(ans))
    n = n - 1