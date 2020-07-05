n, init_t = map(int, input().split())
lst = sorted(map(int, input().split(' ')))
ans = 0
for i in lst:
    ans += init_t * i
    if init_t > 1:
        init_t -= 1
print(ans)
