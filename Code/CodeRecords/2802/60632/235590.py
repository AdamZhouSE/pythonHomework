import math

n, m = map(int, input().split(' '))
wants = list(map(int, input().split(' ')))
times = []
for i in wants:
    times.append(math.ceil(i / m))
times.reverse()
print(n - times.index(max(times)))