n = int(input())
a = int(input())
b = int(input())
c = int(input())
l = []
for i in range(1, 10000):
    if i%a == 0 or i%b == 0 or i%c == 0:
        l.append(i)
if len(l) < 10000:
    print(l[n-1])
else:
    print(1999999984)