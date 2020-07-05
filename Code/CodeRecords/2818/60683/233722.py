val = [int(x) for x in input().split()]
n = val[0]
x = val[1]
chapters = [int(x) for x in input().split()]
chapters.sort()
ans = 0
for i in range(0, n):
    ans += chapters[i] * x
    if x > 1:
        x -= 1
print(ans)
