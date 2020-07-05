a = input()
b = input()
c = input()
a1 = []
b1 = []
c1 = []
for i in a:
    a1.append(i)
for i in b:
    b1.append(i)
for i in c:
    c1.append(i)

if a1 > b1:
    a1, b1 = b1, a1
    a, b = b, a
if b1 > c1:
    b1, c1 = c1, b1
    b, c = c, b
if a1 > b1:
    a1, b1 = b1, a1
    a, b = b, a

print(a)
print(b)
print(c)