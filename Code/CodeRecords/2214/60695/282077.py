s1 = input()
s2 = input()
i = 0
a = 0
b = 0
c = 0
d = 0
m = ""
n = ""
while (s1[i] <= '9' and s1[i] >= '0'):
    a = a * 10 + int(s1[i])
    i += 1
while (s1[i] == '+' or s1[i] == '-'):
    m = m + s1[i]
    i += 1
while (s1[i] != 'i'):
    b = b * 10 + int(s1[i])
    i += 1
i = 0
while (s2[i] <= '9' and s2[i] >= '0'):
    c = c * 10 + int(s2[i])
    i += 1
while (s2[i] == '+' or s2[i] == '-'):
    n = n + s2[i]
    i += 1
while (s2[i] != 'i'):
    d = d * 10 + int(s2[i])
    i += 1
x = a * c
if m != n:
    x += b * d
else:
    x -= b * d
y = 0
if n == '-':
    y -= a * d
else:
    y += a * d
if m == '-':
    y -= b * c
else:
    y += b * c
if m==n and m == "+-":
    print(str(x) + "+-" + str(y) + "i")
else:
    if y >= 0:
        print(str(x) + "+" + str(y) + "i")
    else:
        print(str(x) + str(y) + "i")