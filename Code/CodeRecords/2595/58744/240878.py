t = int(input())
data = list()
for i in range(t):
    data.append([int(d) for d in input().split(' ')])

for d in data:
    n, k = d[0], d[1]
    total = 1
    for i in range(1, n):
        total *= k
    print(total)
