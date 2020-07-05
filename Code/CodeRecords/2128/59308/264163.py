a = [int(x) for x in input().split(',')]
dp2 = 0
dp1 = sum([i*a[i] for i in range(len(a))])
s = sum(a)
ans = dp1
for i in range(1, len(a)):
    dp2 = dp1 + s - len(a)*a[len(a)-i]
    ans = max(ans, dp2)
    dp1 = dp2
print(ans)





