nANDh = input().split()
n = int(nANDh[0])
h = int(nANDh[1])
a = input().split()
for i in range(0, len(a)):
    a[i] = int(a[i])

width = 0

for i in a:
    if i > h:
        width += 2
    else:
        width += 1
print(width)
