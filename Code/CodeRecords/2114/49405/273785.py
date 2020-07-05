aa = []
n = int(input())
aa.append(n)
m = 1
while m * m <= n:
    m += 1
m -= 1
ans = 0
while n > 0:
    while m * m <= n:
        n -= m * m
        ans += 1
        aa.append(m)
    m -= 1
print(ans)
if ans == 4: print(aa)