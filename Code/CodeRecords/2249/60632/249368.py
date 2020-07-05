n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split(','))))
xy = n * n
highest = []
for i in range(n):
    highest.append(max([x[i] for x in data]))
yz = sum(highest)
highest.clear()
for i in range(n):
    highest.append(max(data[i]))
xz = sum(highest)
print(xy + yz + xz)
