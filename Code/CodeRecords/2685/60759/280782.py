ts = int(input())
for t in range(ts):
    n = int(input())
    ans = '0' * n
    while n >= 9:
        ans = '9' + ans
        n -= 9
    ans = (str(n) if n > 0 else '') + ans
    print(ans)
