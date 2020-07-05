a = int(input())
b = int(input())
c = int(input())
A = []
A.append(a)
A.append(b)
A.append(c)
A.sort()
x = A[0]
y = A[1]
z = A[2]
g = y - x - 1 + z - y - 1
if x + 2 == y or y + 2 == z:
    l = 1
else:
    l = (x + 1 != y) + (y + 1 != z)
B = []
B.append(l)
B.append(g)
print(B)
