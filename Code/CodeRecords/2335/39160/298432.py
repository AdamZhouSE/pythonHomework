x = int(input())
y = int(input())

ans = 0
t = y
while t > x:
    if t & 1 == 0:
        ans += 1
        t = t >> 1
    else:
        ans += 2
        t = (t+1) >> 1
ans += x - t
print(ans)

 