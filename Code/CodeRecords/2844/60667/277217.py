f = list(map(int, input().split()))
n = f[0]
t = f[1]
a = list(map(int, input().split()))


maximum = 0
for j in range(n):
    count = 0
    t = f[1]
    for i in range(j,n,1):
        if t >= a[i]:
            t = t - a[i]
            count += 1
        else:
            break
    if count > maximum:
        maximum = count
print(maximum)