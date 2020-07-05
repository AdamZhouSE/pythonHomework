x1 = input().split('+')
a1 = int(x1[0])
b1 = int(x1[1][:-1])
x2 = input().split('+')
a2 = int(x2[0])
b2 = int(x2[1][:-1])
a = a1*a2-b1*b2
b = a1*b2+a2*b1
s = str(a)+'+'+str(b)+'i'
print(s)