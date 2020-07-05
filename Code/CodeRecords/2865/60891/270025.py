n = int(input())
m = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
remain = m
count = 0
while remain > 0:
    remain -= a[count]
    count += 1
print(count)