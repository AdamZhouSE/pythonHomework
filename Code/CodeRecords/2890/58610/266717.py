n, x0, y0 = list(map(int, input().split(' ')))
terrorists = []
for _ in range(n):
    x, y = list(map(int, input().split(' ')))
    k = ((y - y0) / (x - x0) if x != x0 else 'Inf')
    terrorists.append(k)
print(len(set(terrorists)))