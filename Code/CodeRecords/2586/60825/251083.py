x=int(input())
y=int(input())
z=int(input())
a = min(x, y, z)
c = max(x, y, z)
b = x + y + z - a - c
if b - a == 1 and c - b == 1:
    print([0, 0])
elif b - a <= 2 or c - b <= 2:
    print([1, c - a - 2])
else:
    print([2, c - a - 2])