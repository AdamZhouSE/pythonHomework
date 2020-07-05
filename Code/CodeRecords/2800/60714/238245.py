n, d = [int(x) for x in input().split()]
seq = [int(x) for x in input().split()]
times = 0
for i in range(1, n):
    if seq[i] <= seq[i - 1]:
        times += (int((seq[i - 1] - seq[i]) / d) + 1)
        seq[i] += (int((seq[i - 1] - seq[i]) / d) + 1) * d
print(times)
