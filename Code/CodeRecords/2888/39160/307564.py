n, m = map(int, input().split())
a = input().split()
x = a.count("-1")
x = min(x, n-x)
ans = ""
for _ in range(m):
    l, r = map(int, input().split())
    if (r-l) % 2 == 1 and x >= (r-l+1)//2:
        ans = "1"
    else:
        ans = "0"
    print(ans)
