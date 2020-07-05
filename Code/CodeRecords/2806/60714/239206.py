n = int(input())
a, b = [int(x) for x in input().split()]
ans = a * b
for i in range(1, n):
    need, price = [int(x) for x in input().split()]
    if b > price:
        ans += need * price
        b = price
    else:
        ans += need * b
print(ans)
