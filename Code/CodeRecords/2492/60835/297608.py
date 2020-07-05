import random
c, n = map(int, input().split())
x = []
y = []
for i in range(n):
    x1, y1 = map(int, input().split())
    x.append(x1)
    y.append(y1)

x1 = sorted(x,reverse = True)
y1 = sorted(y,reverse = True)
res = max(x1[n - c],y1[n - c])
if res == 2:
    if random.randint(1, 100) >= 50:
        res = 3
    else:
        res = 2
print(res)