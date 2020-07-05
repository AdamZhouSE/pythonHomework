n = int(input())
times = []
for i in range(n):
    times.append(input())
result = 0
for x in set(times):
    if times.count(x) > result:
        result = times.count(x)
print(result)