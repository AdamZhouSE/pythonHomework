m, n = map(int, input().strip('[]').split(','))
i = 0
while m != n:
    m = m >> 1
    n = n >> 1
    i = i + 1
print(m << i)