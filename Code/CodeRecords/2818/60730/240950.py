num, time = map(int, input().split())
m = input().split(" ")
n = list(map(int, m))
n.sort()
ans = 0
for i in range(0, num):
    if time - i > 1:
        ans = ans + (time - i) * n[i]
    else:
        ans = ans + n[i]
print(ans)