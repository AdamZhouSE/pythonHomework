n = int(input())
a = input().split(" ")
for i in range(0, n):
    a[i] = int(a[i])
a = sorted(a)
a.reverse()
long = 0
wide = 0
while len(a) > 0:
    long += a[0]
    a.remove(a[0])
    if len(a) > 0:
        wide += a[len(a) - 1]
        a.remove(a[len(a) - 1])

result = long * long + wide * wide
print(result)