a = input()
a = input().split()
b = []
c = ""

for i in range(len(a)):
    b.append(int(a[i]))
    
b.sort()

for i in range(len(b)):
    c = c+str(b[i])+" "
c = c[0:-1]
print(c)