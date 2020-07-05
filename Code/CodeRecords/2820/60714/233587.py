n = int(input())
time = []
for i in range(0, n):
    time.append(tuple(int(x) for x in input().split()))
frequency = dict()
for i in range(0, n):
    if time[i] in frequency:
        frequency[time[i]] += 1
    else:
        frequency[time[i]] = 1
print(max(frequency.values()))
