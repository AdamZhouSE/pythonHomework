N, i, ans = int(input()), 1, 0
while N > 0:
    ans += N % i == 0
    N -= i
    i += 1
print(ans)
