a = input()
b = c = []
b1 = c1 = 0

a = input().split()
for i in range(len(a)):
    b.append(int(a[i]))
    b1 = b1+int(a[i])
a = input().split()
for i in range(len(a)):
    c.append(int(a[i]))
    c1 = c1 + int(a[i])

c.sort()

if( c[-1]+c[-2] > b1 ):
    print("YES")
else:
    print("NO")