input()
b = []
c = []
d = ""
a = input().split()
for i in range(len(a)):
    b.append(int(a[i]))
b.sort()
a = input().split()
for i in range(len(a)):
    c.append(int(a[i]))

for i in range(len(c)):
    for j in range(len(b)):
        if( b[j] > c[i] ):
            d = d + str(j) + " "
            break
        if( j == len(b)-1 ):
            d = d + str(j+1) + " "

print(d[0:-1])