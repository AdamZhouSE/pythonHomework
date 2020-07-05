n_t = [int(i) for i in input().split()]
n = n_t[0]
t = n_t[1]
a = [int(i) for i in input().split()]
max_n = []
for i in range(n):
    remain = t
    count = 0
    j = i
    while j < n and remain >= a[j]:
        remain -= a[j]
        count += 1
        j += 1
    max_n.append(count)
print(max(max_n))