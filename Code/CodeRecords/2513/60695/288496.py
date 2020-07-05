n = int(input())
m = []
for i in range(0, n):
    a = input().split(",")
    for j in range(0, n):
        m.append(a[j])
k = int(input())
m = list(map(int, m))
m = sorted(m)
print(m[k-1])