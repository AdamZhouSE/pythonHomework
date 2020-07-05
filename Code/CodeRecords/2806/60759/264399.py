n = int(input())
ai = [0 for i in range(n)]
pi = [0 for j in range(n)]
for i in range(n):
    ai[i], pi[i] = map(int, input().split(' '))
price = pi[0]
ans = ai[0] * pi[0]
for i in range(1, n):
    price = min(price, pi[i])
    ans += ai[i] * price
print(ans)
