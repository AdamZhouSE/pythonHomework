n = input().split(" ")
a = input().split(" ")
n[0] = int(n[0])
n[1] = int(n[1])
for i in range(n[0]):
    a[i] = int(a[i])
i = 0
count = 0
while i < n[0]:
    if a[i] > n[1]:
        break
    count += 1
    i += 1
i = n[0]-1
while i >= 0:
    if a[i] > n[1]:
        break
    count += 1
    i -= 1
if count > n[0]:
    count = n[0]
print(count)
