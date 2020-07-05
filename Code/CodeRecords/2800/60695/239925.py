nd = input().split(" ")
n = int(nd[0])
d = int(nd[1])
b = input().split(" ")
for i in range(0, n):
    b[i] = int(b[i])
i = 1
count = 0
while i < n:
    if b[i] <= b[i-1]:
        b[i] += d
        count += 1
    else:
        i += 1
print(count)