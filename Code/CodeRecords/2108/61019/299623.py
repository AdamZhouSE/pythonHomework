read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]
n, r = read(), 0

base = 1
while n >= base:
    change = n % (10 * base)
    change = 0 if change < base \
        else base if change >= 2 * base \
        else (change - base + 1)
    total = (n // (10 * base) * base) + change
    r += total
    base *= 10
print(r)
