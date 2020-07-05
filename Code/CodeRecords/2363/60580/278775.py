import math

n = int(input())
l = []
l1 = []
count = 0

while n//2 > 0:
    l.append(n%2)
    n = n // 2

l.append(n%2)

for i in range(len(l)):
    if l[i] == 0:
        l1.append(1)
    else:
        l1.append(0)

for i in range(len(l1)):
    count += l1[i] * int(math.pow(2, i))

print(count)