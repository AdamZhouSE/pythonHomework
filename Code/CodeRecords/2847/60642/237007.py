a = input()
b = []
c = []
d = 0

a = input().split()
for i in range(len(a)):
    b.append(int(a[i]))
a = input().split()
for i in range(len(a)):
    c.append(int(a[i]))
for i in range(c[0]-1,c[1]-1):
    d = d + b[i]

print(d)