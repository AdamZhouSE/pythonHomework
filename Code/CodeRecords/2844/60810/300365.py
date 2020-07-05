nt = input().split(" ")
n = int(nt[0])
t = int(nt[1])
times = input().split(" ")
for i in range(n):
    times[i] = int(times[i])
res = []
for j in range(n):
    reads=0
    onetime=0
    for i in range(j,n):
        if (t - onetime >= times[i] and i == n - 1):
            reads += 1
            res.append(reads)
            break
        if (t - onetime >= times[i]):
            reads += 1
            onetime += times[i]
        else:
            res.append(reads)
            break
print(max(res))