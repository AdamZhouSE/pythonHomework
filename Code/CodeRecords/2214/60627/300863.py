a = input()[:-1].split('+')
b = input()[:-1].split('+')

a[0] = int(a[0])
a[1] = int(a[1])
b[0] = int(b[0])
b[1] = int(b[1])

x = a[0]*b[0] - a[1]*b[1]
y = a[1]*b[0] + a[0]*b[1]
print(str(x) + '+' + str(y) + 'i')