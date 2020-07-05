a = eval(input())
t = len(a)//3
A = a[0]
B = a[1]
c_A = 0
c_B = 0
res = list()
for i in a:
    if i == A:
        c_A += 1
        continue
    if i == B:
        c_B += 1
        continue
    if c_A == 0:
        A = i
        c_A += 1
        continue
    if c_B == 0:
        B = i
        c_B += 1
        continue
    c_A -= 1
    c_B -= 1
c_A = 0
c_B = 0
for i in a:
    if i == A:
        c_A += 1
    elif i == B:
        c_B += 1
if c_A > t:
    res.append(A)
if c_B > t:
    res.append(B)
print(res)

