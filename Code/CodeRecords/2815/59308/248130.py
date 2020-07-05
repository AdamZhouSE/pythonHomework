n = int(input())
a = [int(x) for x in input().split(' ')]
counts = 0
counts0 = 0
counts1 = 0
for i in a:
    if i > 0:
        counts += i-1
    if i < 0:
        counts += -1 - i
        counts1 += 1
    if i == 0:
        counts0 += 1
if counts1 % 2 == 0:
    counts += counts0
    print(counts)
else:
    if counts0 == 0:
        print(counts + 2)
    else:
        print(counts + counts0)



