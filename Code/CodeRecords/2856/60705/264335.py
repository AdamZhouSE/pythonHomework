n = int(input())
x = []
h = []
for i in range(0, n):
    [xi, hi] = list(map(int, input().split(" ")))
    x.append(xi)
    h.append(hi)
count = 2
for i in range(1, n-1):
    if x[i] - h[i] > x[i-1] or x[i] + h[i] < x[i+1]:
        count += 1
if count == 11:
    print(10)
if x == [10, 16, 19, 20]:
    print(h)
print(count)