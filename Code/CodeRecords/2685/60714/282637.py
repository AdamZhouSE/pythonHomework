T = int(input())
for i in range(0, T):
    n = int(input())
    if n % 9 == 0:
        ans = "9" * (n // 9) + "0" * n
    else:
        ans = str(n % 9) + "9" * (n // 9) + "0" * n
    print(ans)
    