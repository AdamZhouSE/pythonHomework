n = int(input())
a = []
p = []
for i in range(n):
    ai, pi = map(int, input().split(' '))
    a.append(ai)
    p.append(pi)
money = a[0] * p[0]  # 第一天的买肉钱
price = p[0]
for i in range(1, n):
    if p[i] > price:
        money += a[i] * price
    else:
        money += a[i] * p[i]
        price = p[i]
print(money)