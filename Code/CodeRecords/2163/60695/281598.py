n = int(input())
k = int(input())
l = []
s = ''
t = 1
for i in range(0, n):
    t = t * (i + 1)
    l.append(i + 1)

for c in range(0, n - 1):
    t = t / (n - c)
    a = (k - 1) // t
    a = int(a)
    s = s + str(l[a])
    l.remove(l[a])
    k = k % t

s = s + str(l[0])
print(s)