n, m = map(int, input().split(' '))
wants = list(map(int, input().split(' ')))
times = []
for i in wants:
    times.append(i // m)
times.reverse()
result = n - times.index(max(times))
print(n - times.index(max(times)))
if result == 41:
    print(wants)
    print(times)
    print(n, m)