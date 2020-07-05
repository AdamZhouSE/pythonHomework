n = int(input())
res = 0
i = 1
while n // i != 0:
    high = n // (i * 10)
    current = (n // i) % 10
    low = n - (n // i) * i
    if current == 0:
        res += high * i
    elif current == 1:
        res += high * i + low + 1
    else:
        res += (high + 1) * i
    i *= 10
print(res)