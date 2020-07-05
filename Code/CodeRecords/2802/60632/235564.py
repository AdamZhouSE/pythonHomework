n, m = map(int, input().split(' '))
wants = list(map(int, input().split(' ')))
times = []
for i in wants:
    times.append(i // m)
times.reverse()
print(n - times.index(max(times)))